from datetime import datetime, timedelta, timezone
from functools import wraps

import jwt
from flask import current_app, g, request

from app.common.errors import ApiError


def create_token(user_id):
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(seconds=current_app.config["JWT_TTL_SECONDS"]),
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")


def auth_required(view):
    """从 Authorization: Bearer <token> 取 userId，业务层只认 g.user_id。"""

    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        token = header[7:].strip() if header.startswith("Bearer ") else ""
        if not token:
            raise ApiError("UNAUTHORIZED", "缺少登录态", 401)
        try:
            payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            g.user_id = int(payload["sub"])
        except (jwt.PyJWTError, KeyError, ValueError):
            raise ApiError("UNAUTHORIZED", "登录态无效或已过期", 401) from None
        return view(*args, **kwargs)

    return wrapper

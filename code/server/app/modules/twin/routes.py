"""twin 路由声明：只声明接口与契约，业务待团队按 功能实现规格书.md 实现（当前统一 501）。"""

from flask import Blueprint

from app.common.auth import auth_required
from app.common.response import failure

bp = Blueprint("twin", __name__, url_prefix="/api/v1/twin")


def _todo(path, func, owner, sprint, spec):
    message = f"twin {path}：负责人 {owner} / Sprint {sprint} / 功能 {func} / 规格书 {spec}"
    return failure("NOT_IMPLEMENTED", message, 501)

@bp.post("/config")
@auth_required
def select_avatar():
    return _todo("POST /config", "TWN-02", "B", "W3", "§3 TWN-02")

@bp.get("/profile")
@auth_required
def get_profile():
    return _todo("GET /profile", "TWN-07", "B", "W3", "§3 TWN-07")

@bp.get("/messages")
@auth_required
def list_messages():
    return _todo("GET /messages", "TWN-08", "B", "W3", "§3 TWN-08")

@bp.post("/messages")
@auth_required
def send_message():
    return _todo("POST /messages", "TWN-03", "B", "W3", "§3 TWN-03")

@bp.post("/memory/search")
@auth_required
def search_memory():
    return _todo("POST /memory/search", "TWN-04", "B", "后续", "后续版本")

@bp.get("/proactive")
@auth_required
def list_proactive():
    return _todo("GET /proactive", "TWN-06", "B", "后续", "后续版本")

@bp.post("/intimacy")
@auth_required
def add_intimacy():
    return _todo("POST /intimacy", "TWN-07", "B", "W3", "§3 TWN-07")

@bp.get("/mood")
@auth_required
def get_mood():
    return _todo("GET /mood", "TWN-05", "B", "后续", "§3 TWN-05")

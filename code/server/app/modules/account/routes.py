"""account 路由声明：只声明接口与契约，业务待团队按 功能实现规格书.md 实现（当前统一 501）。"""

from flask import Blueprint

from app.common.auth import auth_required
from app.common.response import failure

bp = Blueprint("account", __name__, url_prefix="/api/v1/account")


def _todo(path, func, owner, sprint, spec):
    message = f"account {path}：负责人 {owner} / Sprint {sprint} / 功能 {func} / 规格书 {spec}"
    return failure("NOT_IMPLEMENTED", message, 501)

@bp.post("/otp/send")
def send_otp():
    return _todo("POST /otp/send", "ACC-01", "B", "W1", "§1 ACC-01")

@bp.post("/login")
def login():
    return _todo("POST /login", "ACC-01", "B", "W1", "§1 ACC-01")

@bp.get("/me")
@auth_required
def get_me():
    return _todo("GET /me", "ACC-03", "B", "W1", "§1 ACC-03")

@bp.patch("/me")
@auth_required
def update_me():
    return _todo("PATCH /me", "ACC-03", "B", "W1", "§1 ACC-03")

@bp.get("/profile")
@auth_required
def get_profile():
    return _todo("GET /profile", "ACC-06", "B", "W2", "§1 ACC-06")

@bp.put("/privacy")
@auth_required
def update_privacy():
    return _todo("PUT /privacy", "ACC-06", "B", "W2", "§1 ACC-06")

@bp.post("/questionnaire")
@auth_required
def submit_questionnaire():
    return _todo("POST /questionnaire", "ACC-04", "B", "W2", "§1 ACC-04")

@bp.get("/devices")
@auth_required
def list_devices():
    return _todo("GET /devices", "ACC-07", "B", "W2", "§1 ACC-07")

"""solve 路由声明：只声明接口与契约，业务待团队按 功能实现规格书.md 实现（当前统一 501）。"""

from flask import Blueprint

from app.common.auth import auth_required
from app.common.response import failure

bp = Blueprint("solve", __name__, url_prefix="/api/v1/solve")


def _todo(path, func, owner, sprint, spec):
    message = f"solve {path}：负责人 {owner} / Sprint {sprint} / 功能 {func} / 规格书 {spec}"
    return failure("NOT_IMPLEMENTED", message, 501)

@bp.post("/ocr")
@auth_required
def ocr():
    return _todo("POST /ocr", "SLV-01", "C", "W3", "§5 SLV-01")

@bp.post("/sessions")
@auth_required
def create_session():
    return _todo("POST /sessions", "SLV-03", "C", "W3", "§5 SLV-03")

@bp.get("/sessions/<int:session_id>")
@auth_required
def get_session(session_id):
    return _todo("GET /sessions/{id}", "SLV-03", "C", "W3", "§5 SLV-03")

@bp.get("/sessions")
@auth_required
def list_sessions():
    return _todo("GET /sessions", "SLV-06", "C", "后续", "后续版本")

@bp.post("/wrongs")
@auth_required
def create_wrong():
    return _todo("POST /wrongs", "SLV-04", "C", "W3", "§5 SLV-04")

@bp.get("/wrongs")
@auth_required
def list_wrongs():
    return _todo("GET /wrongs", "SLV-05", "C", "W3", "§5 SLV-05")

@bp.patch("/wrongs/<int:wrong_id>")
@auth_required
def update_wrong(wrong_id):
    return _todo("PATCH /wrongs/{id}", "SLV-05", "C", "W3", "§5 SLV-05")

@bp.delete("/wrongs/<int:wrong_id>")
@auth_required
def delete_wrong(wrong_id):
    return _todo("DELETE /wrongs/{id}", "SLV-05", "C", "W3", "§5 SLV-05")

@bp.post("/hints")
@auth_required
def hints():
    return _todo("POST /hints", "SLV-07", "C", "后续", "后续版本")

@bp.post("/variants")
@auth_required
def variants():
    return _todo("POST /variants", "SLV-08", "C", "后续", "后续版本")

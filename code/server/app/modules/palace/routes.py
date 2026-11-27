"""palace 路由声明：只声明接口与契约，业务待团队按 功能实现规格书.md 实现（当前统一 501）。"""

from flask import Blueprint

from app.common.auth import auth_required
from app.common.response import failure

bp = Blueprint("palace", __name__, url_prefix="/api/v1/palace")


def _todo(path, func, owner, sprint, spec):
    message = f"palace {path}：负责人 {owner} / Sprint {sprint} / 功能 {func} / 规格书 {spec}"
    return failure("NOT_IMPLEMENTED", message, 501)

@bp.get("/room")
@auth_required
def get_room():
    return _todo("GET /room", "PLS-01", "C", "W4", "§6 PLS-01")

@bp.post("/items")
@auth_required
def create_item():
    return _todo("POST /items", "PLS-02", "C", "W4", "§6 PLS-02")

@bp.patch("/items/<int:item_id>")
@auth_required
def update_item(item_id):
    return _todo("PATCH /items/{id}", "PLS-05", "C", "W4", "§6 PLS-05")

@bp.delete("/items/<int:item_id>")
@auth_required
def delete_item(item_id):
    return _todo("DELETE /items/{id}", "PLS-05", "C", "W4", "§6 PLS-05")

@bp.post("/items/<int:item_id>/link")
@auth_required
def link_item(item_id):
    return _todo("POST /items/{id}/link", "PLS-03", "C", "W4", "§6 PLS-03")

@bp.post("/items/<int:item_id>/review")
@auth_required
def review_item(item_id):
    return _todo("POST /items/{id}/review", "PLS-04", "C", "W4", "§6 PLS-04")

@bp.get("/items")
@auth_required
def list_items():
    return _todo("GET /items", "PLS-05", "C", "W4", "§6 PLS-05")

@bp.get("/rewards")
@auth_required
def list_rewards():
    return _todo("GET /rewards", "PLS-06", "C", "后续", "后续版本")

@bp.patch("/room")
@auth_required
def update_theme():
    return _todo("PATCH /room", "PLS-07", "C", "后续", "后续版本")

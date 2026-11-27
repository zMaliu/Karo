"""brain 路由声明：只声明接口与契约，业务待团队按 功能实现规格书.md 实现（当前统一 501）。"""

from flask import Blueprint

from app.common.auth import auth_required
from app.common.response import failure

bp = Blueprint("brain", __name__, url_prefix="/api/v1/brain")


def _todo(path, func, owner, sprint, spec):
    message = f"brain {path}：负责人 {owner} / Sprint {sprint} / 功能 {func} / 规格书 {spec}"
    return failure("NOT_IMPLEMENTED", message, 501)

@bp.post("/files")
@auth_required
def upload_file():
    return _todo("POST /files", "BRN-01", "B", "W4", "§4 BRN-01")

@bp.get("/files")
@auth_required
def list_files():
    return _todo("GET /files", "BRN-05", "B", "W4", "§4 BRN-05")

@bp.get("/files/<int:file_id>")
@auth_required
def get_file(file_id):
    return _todo("GET /files/{id}", "BRN-01", "B", "W4", "§4 BRN-01")

@bp.post("/notes")
@auth_required
def create_note():
    return _todo("POST /notes", "BRN-02", "B", "W4", "§4 BRN-02")

@bp.get("/notes/<int:note_id>")
@auth_required
def get_note(note_id):
    return _todo("GET /notes/{id}", "BRN-02", "B", "W4", "§4 BRN-02")

@bp.patch("/notes/<int:note_id>")
@auth_required
def update_note(note_id):
    return _todo("PATCH /notes/{id}", "BRN-06", "B", "后续", "后续版本")

@bp.post("/diaries")
@auth_required
def create_diary():
    return _todo("POST /diaries", "BRN-03", "B", "W4", "§4 BRN-03")

@bp.get("/diaries")
@auth_required
def list_diaries():
    return _todo("GET /diaries", "BRN-03", "B", "W4", "§4 BRN-03")

@bp.post("/chat")
@auth_required
def chat():
    return _todo("POST /chat", "BRN-04", "B", "后续", "后续版本")

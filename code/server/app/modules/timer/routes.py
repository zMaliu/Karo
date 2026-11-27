"""timer 路由声明：只声明接口与契约，业务待团队按 功能实现规格书.md 实现（当前统一 501）。"""

from flask import Blueprint

from app.common.auth import auth_required
from app.common.response import failure

bp = Blueprint("timer", __name__, url_prefix="/api/v1/timer")


def _todo(path, func, owner, sprint, spec):
    message = f"timer {path}：负责人 {owner} / Sprint {sprint} / 功能 {func} / 规格书 {spec}"
    return failure("NOT_IMPLEMENTED", message, 501)

@bp.post("/sessions")
@auth_required
def create_session():
    return _todo("POST /sessions", "TMR-01", "C", "W1", "§2 TMR-01")

@bp.patch("/sessions/<int:session_id>")
@auth_required
def update_session(session_id):
    return _todo("PATCH /sessions/{id}", "TMR-01", "C", "W1", "§2 TMR-01")

@bp.post("/sessions/<int:session_id>/complete")
@auth_required
def complete_session(session_id):
    return _todo("POST /sessions/{id}/complete", "TMR-07", "C", "W1", "§2 TMR-07")

@bp.post("/sessions/<int:session_id>/abort")
@auth_required
def abort_session(session_id):
    return _todo("POST /sessions/{id}/abort", "TMR-02", "C", "W1", "§2 TMR-01")

@bp.get("/sessions/active")
@auth_required
def active_session():
    return _todo("GET /sessions/active", "TMR-08", "C", "W1", "§2 TMR-08")

@bp.get("/sessions")
@auth_required
def list_sessions():
    return _todo("GET /sessions", "TMR-08", "C", "W1", "§2 TMR-08")

@bp.get("/stats")
@auth_required
def get_stats():
    return _todo("GET /stats", "TMR-08", "C", "W1", "§2 TMR-08")

@bp.post("/sessions/<int:session_id>/interrupt")
@auth_required
def report_interrupt(session_id):
    return _todo("POST /sessions/{id}/interrupt", "TMR-05", "C", "W2", "§2 TMR-05")

@bp.get("/stats/month")
@auth_required
def get_month_stats():
    return _todo("GET /stats/month", "TMR-08", "C", "W2", "§2 TMR-08")

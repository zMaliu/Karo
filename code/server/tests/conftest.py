import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import create_app  # noqa: E402
from app.common.auth import create_token  # noqa: E402
from app.config import TestingConfig  # noqa: E402

TZ_HEADER = {"X-Client-Timezone": "Asia/Shanghai"}

# 53 端点契约（唯一清单）：module / method / rule / 功能编号 / 负责人 / Sprint / 规格书章节 / 是否公开
ENDPOINTS = [
    ("account", "POST", "/api/v1/account/otp/send", "ACC-01", "B", "W1", "§1 ACC-01", True),
    ("account", "POST", "/api/v1/account/login", "ACC-01", "B", "W1", "§1 ACC-01", True),
    ("account", "GET", "/api/v1/account/me", "ACC-03", "B", "W1", "§1 ACC-03", False),
    ("account", "PATCH", "/api/v1/account/me", "ACC-03", "B", "W1", "§1 ACC-03", False),
    ("account", "GET", "/api/v1/account/profile", "ACC-06", "B", "W2", "§1 ACC-06", False),
    ("account", "PUT", "/api/v1/account/privacy", "ACC-06", "B", "W2", "§1 ACC-06", False),
    ("account", "POST", "/api/v1/account/questionnaire", "ACC-04", "B", "W2", "§1 ACC-04", False),
    ("account", "GET", "/api/v1/account/devices", "ACC-07", "B", "W2", "§1 ACC-07", False),
    ("timer", "POST", "/api/v1/timer/sessions", "TMR-01", "C", "W1", "§2 TMR-01", False),
    ("timer", "PATCH", "/api/v1/timer/sessions/<int:session_id>", "TMR-01", "C", "W1", "§2 TMR-01", False),
    ("timer", "POST", "/api/v1/timer/sessions/<int:session_id>/complete", "TMR-07", "C", "W1", "§2 TMR-07", False),
    ("timer", "POST", "/api/v1/timer/sessions/<int:session_id>/abort", "TMR-02", "C", "W1", "§2 TMR-01", False),
    ("timer", "GET", "/api/v1/timer/sessions/active", "TMR-08", "C", "W1", "§2 TMR-08", False),
    ("timer", "GET", "/api/v1/timer/sessions", "TMR-08", "C", "W1", "§2 TMR-08", False),
    ("timer", "GET", "/api/v1/timer/stats", "TMR-08", "C", "W1", "§2 TMR-08", False),
    ("timer", "POST", "/api/v1/timer/sessions/<int:session_id>/interrupt", "TMR-05", "C", "W2", "§2 TMR-05", False),
    ("timer", "GET", "/api/v1/timer/stats/month", "TMR-08", "C", "W2", "§2 TMR-08", False),
    ("twin", "POST", "/api/v1/twin/config", "TWN-02", "B", "W3", "§3 TWN-02", False),
    ("twin", "GET", "/api/v1/twin/profile", "TWN-07", "B", "W3", "§3 TWN-07", False),
    ("twin", "GET", "/api/v1/twin/messages", "TWN-08", "B", "W3", "§3 TWN-08", False),
    ("twin", "POST", "/api/v1/twin/messages", "TWN-03", "B", "W3", "§3 TWN-03", False),
    ("twin", "POST", "/api/v1/twin/memory/search", "TWN-04", "B", "后续", "后续版本", False),
    ("twin", "GET", "/api/v1/twin/proactive", "TWN-06", "B", "后续", "后续版本", False),
    ("twin", "POST", "/api/v1/twin/intimacy", "TWN-07", "B", "W3", "§3 TWN-07", False),
    ("twin", "GET", "/api/v1/twin/mood", "TWN-05", "B", "后续", "§3 TWN-05", False),
    ("brain", "POST", "/api/v1/brain/files", "BRN-01", "B", "W4", "§4 BRN-01", False),
    ("brain", "GET", "/api/v1/brain/files", "BRN-05", "B", "W4", "§4 BRN-05", False),
    ("brain", "GET", "/api/v1/brain/files/<int:file_id>", "BRN-01", "B", "W4", "§4 BRN-01", False),
    ("brain", "POST", "/api/v1/brain/notes", "BRN-02", "B", "W4", "§4 BRN-02", False),
    ("brain", "GET", "/api/v1/brain/notes/<int:note_id>", "BRN-02", "B", "W4", "§4 BRN-02", False),
    ("brain", "PATCH", "/api/v1/brain/notes/<int:note_id>", "BRN-06", "B", "后续", "后续版本", False),
    ("brain", "POST", "/api/v1/brain/diaries", "BRN-03", "B", "W4", "§4 BRN-03", False),
    ("brain", "GET", "/api/v1/brain/diaries", "BRN-03", "B", "W4", "§4 BRN-03", False),
    ("brain", "POST", "/api/v1/brain/chat", "BRN-04", "B", "后续", "后续版本", False),
    ("solve", "POST", "/api/v1/solve/ocr", "SLV-01", "C", "W3", "§5 SLV-01", False),
    ("solve", "POST", "/api/v1/solve/sessions", "SLV-03", "C", "W3", "§5 SLV-03", False),
    ("solve", "GET", "/api/v1/solve/sessions/<int:session_id>", "SLV-03", "C", "W3", "§5 SLV-03", False),
    ("solve", "GET", "/api/v1/solve/sessions", "SLV-06", "C", "后续", "后续版本", False),
    ("solve", "POST", "/api/v1/solve/wrongs", "SLV-04", "C", "W3", "§5 SLV-04", False),
    ("solve", "GET", "/api/v1/solve/wrongs", "SLV-05", "C", "W3", "§5 SLV-05", False),
    ("solve", "PATCH", "/api/v1/solve/wrongs/<int:wrong_id>", "SLV-05", "C", "W3", "§5 SLV-05", False),
    ("solve", "DELETE", "/api/v1/solve/wrongs/<int:wrong_id>", "SLV-05", "C", "W3", "§5 SLV-05", False),
    ("solve", "POST", "/api/v1/solve/hints", "SLV-07", "C", "后续", "后续版本", False),
    ("solve", "POST", "/api/v1/solve/variants", "SLV-08", "C", "后续", "后续版本", False),
    ("palace", "GET", "/api/v1/palace/room", "PLS-01", "C", "W4", "§6 PLS-01", False),
    ("palace", "POST", "/api/v1/palace/items", "PLS-02", "C", "W4", "§6 PLS-02", False),
    ("palace", "PATCH", "/api/v1/palace/items/<int:item_id>", "PLS-05", "C", "W4", "§6 PLS-05", False),
    ("palace", "DELETE", "/api/v1/palace/items/<int:item_id>", "PLS-05", "C", "W4", "§6 PLS-05", False),
    ("palace", "POST", "/api/v1/palace/items/<int:item_id>/link", "PLS-03", "C", "W4", "§6 PLS-03", False),
    ("palace", "POST", "/api/v1/palace/items/<int:item_id>/review", "PLS-04", "C", "W4", "§6 PLS-04", False),
    ("palace", "GET", "/api/v1/palace/items", "PLS-05", "C", "W4", "§6 PLS-05", False),
    ("palace", "GET", "/api/v1/palace/rewards", "PLS-06", "C", "后续", "后续版本", False),
    ("palace", "PATCH", "/api/v1/palace/room", "PLS-07", "C", "后续", "后续版本", False),
]


@pytest.fixture()
def app():
    return create_app(TestingConfig)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def token(app):
    with app.app_context():
        return create_token(1)


def auth(token):
    return {**TZ_HEADER, "Authorization": "Bearer " + token}


def url_of(rule):
    """把 /timer/sessions/<int:session_id> 转成可请求的 /timer/sessions/1。"""
    return re.sub(r"<int:\w+>", "1", rule)

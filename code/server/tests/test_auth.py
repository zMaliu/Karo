from conftest import TZ_HEADER, auth

PROTECTED = "/api/v1/timer/stats"


def test_missing_token_401(client):
    resp = client.get(PROTECTED, headers=TZ_HEADER)
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "UNAUTHORIZED"


def test_forged_token_401(client):
    resp = client.get(PROTECTED, headers={**TZ_HEADER, "Authorization": "Bearer forged.token.value"})
    assert resp.status_code == 401
    assert resp.get_json()["error"]["code"] == "UNAUTHORIZED"


def test_valid_token_passes_auth_to_501(client, token):
    resp = client.get(PROTECTED, headers=auth(token))
    assert resp.status_code == 501
    assert resp.get_json()["error"]["code"] == "NOT_IMPLEMENTED"

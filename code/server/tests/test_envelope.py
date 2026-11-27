from conftest import TZ_HEADER, auth


def test_envelope_structure_for_501_and_401(client, token):
    resp_501 = client.get("/api/v1/twin/profile", headers=auth(token))
    resp_401 = client.get("/api/v1/twin/profile", headers=TZ_HEADER)
    for resp in (resp_501, resp_401):
        body = resp.get_json()
        assert set(body) == {"error", "meta"}
        assert set(body["error"]) == {"code", "message"}
        assert "server_time" in body["meta"]
    assert resp_501.get_json()["error"]["code"] == "NOT_IMPLEMENTED"
    assert resp_401.get_json()["error"]["code"] == "UNAUTHORIZED"

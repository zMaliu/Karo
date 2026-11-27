

def test_missing_timezone_header_400(client):
    resp = client.get("/api/v1/timer/stats")
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "TIMEZONE_REQUIRED"


def test_invalid_timezone_header_400(client):
    resp = client.get("/api/v1/timer/stats", headers={"X-Client-Timezone": "Mars/Olympus"})
    assert resp.status_code == 400
    assert resp.get_json()["error"]["code"] == "TIMEZONE_INVALID"

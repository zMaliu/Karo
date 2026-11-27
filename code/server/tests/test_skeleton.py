from conftest import ENDPOINTS, TZ_HEADER, auth, url_of


def test_every_endpoint_returns_501_with_function_id(client, token):
    for module, method, rule, fid, owner, sprint, spec, public in ENDPOINTS:
        headers = dict(TZ_HEADER) if public else auth(token)
        url = url_of(rule)
        if method == 'GET':
            resp = client.get(url, headers=headers)
        elif method == 'DELETE':
            resp = client.delete(url, headers=headers)
        elif method == 'PATCH':
            resp = client.patch(url, json={}, headers=headers)
        elif method == 'PUT':
            resp = client.put(url, json={}, headers=headers)
        else:
            resp = client.post(url, json={}, headers=headers)
        assert resp.status_code == 501, (method, rule, resp.status_code)
        error = resp.get_json()["error"]
        assert error["code"] == "NOT_IMPLEMENTED"
        assert fid in error["message"]
        assert "负责人 " + owner in error["message"]
        assert spec in error["message"]

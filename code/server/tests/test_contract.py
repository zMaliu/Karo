from conftest import ENDPOINTS


def test_contract_endpoints_registered(app):
    registered = set()
    for rule in app.url_map.iter_rules():
        if not rule.rule.startswith("/api/v1/"):
            continue
        for method in rule.methods:
            if method in {"HEAD", "OPTIONS"}:
                continue
            registered.add((rule.rule, method))
    expected = {(e[2], e[1]) for e in ENDPOINTS}
    assert len(expected) == 53
    assert registered == expected


def test_route_count_and_six_blueprints(app):
    rules = [r for r in app.url_map.iter_rules() if r.rule.startswith("/api/v1/")]
    assert len(rules) == 53
    assert set(app.blueprints) == {"account", "timer", "twin", "brain", "solve", "palace"}

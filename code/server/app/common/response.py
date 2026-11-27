from datetime import datetime, timezone

from flask import g, has_request_context, jsonify


def iso_utc(dt):
    """库里的时间统一存 UTC naive，出参补 Z，客户端按本地时区展示。"""
    if dt is None:
        return None
    return dt.isoformat(timespec="seconds") + "Z"


def _meta(extra=None):
    server_time = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    meta = {"server_time": server_time}
    if has_request_context() and getattr(g, "client_tz_name", None):
        meta["timezone"] = g.client_tz_name
    meta.update(extra or {})
    return meta


def success(data, status=200, **meta):
    return jsonify({"data": data, "meta": _meta(meta)}), status


def failure(code, message, status=400):
    return jsonify({"error": {"code": code, "message": message}, "meta": _meta()}), status

"""twin 请求 Schema 声明（团队实现端点时在 routes 中 Schema().load() 使用）。"""

from marshmallow import EXCLUDE, Schema, fields, validate


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class TwinConfigSchema(BaseSchema):
    """POST /twin/config（TWN-02）：avatar_id 必填。"""
    avatar_id = fields.String(required=True, validate=validate.OneOf(["a1", "a2", "a3"]))

class TwinProfileQuerySchema(BaseSchema):
    """GET /twin/profile（TWN-07）：无入参。"""

class MessageListQuerySchema(BaseSchema):
    """GET /twin/messages（TWN-08）：before_id/limit 可选。"""
    before_id = fields.Integer(validate=validate.Range(min=1))
    limit = fields.Integer(load_default=20, validate=validate.Range(min=1, max=50))

class TwinMessageSchema(BaseSchema):
    """POST /twin/messages（TWN-03）：content 必填 1-500 字。"""
    content = fields.String(required=True, validate=validate.Length(min=1, max=500))

class MemorySearchSchema(BaseSchema):
    """POST /twin/memory/search（TWN-04）：query 必填。"""
    query = fields.String(required=True, validate=validate.Length(min=1, max=100))
    top_k = fields.Integer(load_default=5, validate=validate.Range(min=1, max=10))

class ProactiveQuerySchema(BaseSchema):
    """GET /twin/proactive（TWN-06）：无入参。"""

class IntimacySchema(BaseSchema):
    """POST /twin/intimacy（TWN-07）：event_type 必填。"""
    event_type = fields.String(required=True, validate=validate.OneOf(["chat", "proactive_click", "daily_login"]))

class MoodQuerySchema(BaseSchema):
    """GET /twin/mood（TWN-05）：无入参。"""

"""timer 请求 Schema 声明（团队实现端点时在 routes 中 Schema().load() 使用）。"""

from marshmallow import EXCLUDE, Schema, fields, validate


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class SessionCreateSchema(BaseSchema):
    """POST /timer/sessions（TMR-01）：mode 必填。"""
    mode = fields.String(required=True, validate=validate.OneOf(["pomodoro", "focus", "countdown"]))
    subject_tag = fields.String(load_default="未分类", validate=validate.Length(max=32))
    planned_sec = fields.Integer(validate=validate.Range(min=60, max=14400))

class SessionUpdateSchema(BaseSchema):
    """PATCH /timer/sessions/{id}（TMR-01）：action 必填。"""
    action = fields.String(required=True, validate=validate.OneOf(["pause", "resume", "heartbeat"]))

class CompleteSchema(BaseSchema):
    """POST /timer/sessions/{id}/complete（TMR-07）：无 body，幂等键走 Idempotency-Key 头。"""

class AbortSchema(BaseSchema):
    """POST /timer/sessions/{id}/abort（TMR-01）：无入参。"""

class ActiveSessionQuerySchema(BaseSchema):
    """GET /timer/sessions/active（TMR-08）：无入参。"""

class SessionListQuerySchema(BaseSchema):
    """GET /timer/sessions（TMR-08）：limit 可选。"""
    limit = fields.Integer(load_default=20, validate=validate.Range(min=1, max=50))

class StatsQuerySchema(BaseSchema):
    """GET /timer/stats（TMR-08）：range=today|week。"""
    range = fields.String(load_default="today", validate=validate.OneOf(["today", "week"]))

class InterruptSchema(BaseSchema):
    """POST /timer/sessions/{id}/interrupt（TMR-05）：count 可选。"""
    count = fields.Integer(load_default=1, validate=validate.Range(min=1, max=99))

class MonthStatsQuerySchema(BaseSchema):
    """GET /timer/stats/month（TMR-08）：month=YYYY-MM 可选。"""
    month = fields.String(validate=validate.Length(equal=7))

"""account 请求 Schema 声明（团队实现端点时在 routes 中 Schema().load() 使用）。"""

from marshmallow import EXCLUDE, Schema, fields, validate


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class OtpSendSchema(BaseSchema):
    """POST /account/otp/send（ACC-01）：phone 必填，11 位手机号。"""
    phone = fields.String(required=True, validate=validate.Length(equal=11))

class LoginSchema(BaseSchema):
    """POST /account/login（ACC-01）：phone + 6 位 code。"""
    phone = fields.String(required=True, validate=validate.Length(equal=11))
    code = fields.String(required=True, validate=validate.Length(equal=6))

class MeQuerySchema(BaseSchema):
    """GET /account/me（ACC-03）：无入参，userId 只从 JWT 取。"""

class MeUpdateSchema(BaseSchema):
    """PATCH /account/me（ACC-03）：资料白名单字段，全部可选。"""
    nickname = fields.String(validate=validate.Length(max=20))
    avatar_url = fields.String(validate=validate.Length(max=255))
    grade = fields.String(validate=validate.Length(max=16))
    major = fields.String(validate=validate.Length(max=32))
    goal = fields.String(validate=validate.Length(max=128))

class ProfileQuerySchema(BaseSchema):
    """GET /account/profile（ACC-06）：无入参。"""

class PrivacySchema(BaseSchema):
    """PUT /account/privacy（ACC-06）：三个隐私开关，至少传一个。"""
    show_online = fields.Boolean()
    personalized_rec = fields.Boolean()
    push_enabled = fields.Boolean()

class QuestionnaireSchema(BaseSchema):
    """POST /account/questionnaire（ACC-04）：25 题答案必填。"""
    answers = fields.List(fields.Dict(), required=True, validate=validate.Length(equal=25))
    questionnaire_version = fields.String(validate=validate.Length(max=16))

class DevicesQuerySchema(BaseSchema):
    """GET /account/devices（ACC-07）：无入参。"""

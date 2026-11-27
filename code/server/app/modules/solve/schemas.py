"""solve 请求 Schema 声明（团队实现端点时在 routes 中 Schema().load() 使用）。"""

from marshmallow import EXCLUDE, Schema, fields, validate


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class OcrSchema(BaseSchema):
    """POST /solve/ocr（SLV-01）：图片文件必填 + 可选科目。"""
    file = fields.Raw(required=True)
    subject_tag = fields.String(validate=validate.Length(max=32))

class SolveCreateSchema(BaseSchema):
    """POST /solve/sessions（SLV-03）：提交题目求解。"""
    source = fields.String(required=True, validate=validate.OneOf(["photo", "manual"]))
    subject_tag = fields.String(validate=validate.Length(max=32))
    question_text = fields.String(required=True, validate=validate.Length(min=1, max=2000))
    image_url = fields.String(validate=validate.Length(max=255))

class SolveDetailQuerySchema(BaseSchema):
    """GET /solve/sessions/{id}（SLV-03）：无入参。"""

class SessionListSchema(BaseSchema):
    """GET /solve/sessions（SLV-06）：科目 + 分页。"""
    subject_tag = fields.String(validate=validate.Length(max=32))
    page = fields.Integer(load_default=1, validate=validate.Range(min=1))

class WrongCreateSchema(BaseSchema):
    """POST /solve/wrongs（SLV-04）：session_id 必填，错因可选。"""
    session_id = fields.Integer(required=True, validate=validate.Range(min=1))
    wrong_reason = fields.String(validate=validate.Length(max=500))

class WrongListSchema(BaseSchema):
    """GET /solve/wrongs（SLV-05）：科目/复习状态筛选。"""
    subject_tag = fields.String(validate=validate.Length(max=32))
    review_status = fields.String(validate=validate.OneOf(["new", "reviewed", "mastered"]))

class WrongUpdateSchema(BaseSchema):
    """PATCH /solve/wrongs/{id}（SLV-05）：错因/复习状态可选。"""
    wrong_reason = fields.String(validate=validate.Length(max=500))
    review_status = fields.String(validate=validate.OneOf(["new", "reviewed", "mastered"]))

class WrongDeleteQuerySchema(BaseSchema):
    """DELETE /solve/wrongs/{id}（SLV-05）：无入参（二次确认由前端做）。"""

class HintSchema(BaseSchema):
    """POST /solve/hints（SLV-07）：引导式分步求解。"""
    session_id = fields.Integer(required=True, validate=validate.Range(min=1))
    step = fields.Integer(required=True, validate=validate.Range(min=1, max=3))
    stuck_point = fields.String(validate=validate.Length(max=200))

class VariantSchema(BaseSchema):
    """POST /solve/variants（SLV-08）：变式题推荐（V0.5）。"""
    wrong_id = fields.Integer(required=True, validate=validate.Range(min=1))
    count = fields.Integer(load_default=3, validate=validate.Range(min=1, max=5))

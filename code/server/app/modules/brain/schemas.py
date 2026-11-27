"""brain 请求 Schema 声明（团队实现端点时在 routes 中 Schema().load() 使用）。"""

from marshmallow import EXCLUDE, Schema, fields, validate


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class FileUploadSchema(BaseSchema):
    """POST /brain/files（BRN-01）：multipart 文件 + 可选科目标签。"""
    file = fields.Raw(required=True)
    subject_tag = fields.String(validate=validate.Length(max=32))

class FileListSchema(BaseSchema):
    """GET /brain/files（BRN-05）：关键词/类型/科目筛选 + 分页。"""
    keyword = fields.String(validate=validate.Length(max=64))
    file_type = fields.String(validate=validate.OneOf(["pdf", "image", "word", "txt"]))
    subject_tag = fields.String(validate=validate.Length(max=32))
    page = fields.Integer(load_default=1, validate=validate.Range(min=1))

class FileDetailQuerySchema(BaseSchema):
    """GET /brain/files/{id}（BRN-01）：无入参。"""

class NoteCreateSchema(BaseSchema):
    """POST /brain/notes（BRN-02）：标题 + Markdown 正文。"""
    title = fields.String(required=True, validate=validate.Length(min=1, max=128))
    content_md = fields.String(required=True, validate=validate.Length(min=1, max=20000))
    tags = fields.List(fields.String(), load_default=list)

class NoteDetailQuerySchema(BaseSchema):
    """GET /brain/notes/{id}（BRN-02）：无入参。"""

class NoteUpdateSchema(BaseSchema):
    """PATCH /brain/notes/{id}（BRN-06）：标题/正文/标签均可选。"""
    title = fields.String(validate=validate.Length(max=128))
    content_md = fields.String(validate=validate.Length(max=20000))
    tags = fields.List(fields.String())

class DiaryCreateSchema(BaseSchema):
    """POST /brain/diaries（BRN-03）：日期 + 正文 + 心情。"""
    entry_date = fields.Date(required=True)
    mood = fields.String(validate=validate.Length(max=16))
    content = fields.String(required=True, validate=validate.Length(min=1, max=2000))

class DiaryListSchema(BaseSchema):
    """GET /brain/diaries（BRN-03）：日期范围 + 分页。"""
    start_date = fields.Date()
    end_date = fields.Date()
    page = fields.Integer(load_default=1, validate=validate.Range(min=1))

class ChatSchema(BaseSchema):
    """POST /brain/chat（BRN-04）：question 必填 + 检索范围。"""
    question = fields.String(required=True, validate=validate.Length(min=1, max=500))
    scope = fields.String(load_default="all", validate=validate.OneOf(["file", "note", "all"]))

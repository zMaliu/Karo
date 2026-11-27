"""palace 请求 Schema 声明（团队实现端点时在 routes 中 Schema().load() 使用）。"""

from marshmallow import EXCLUDE, Schema, fields, validate


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class RoomQuerySchema(BaseSchema):
    """GET /palace/room（PLS-01）：无入参。"""

class ItemCreateSchema(BaseSchema):
    """POST /palace/items（PLS-02）：摆放物品。"""
    item_type = fields.String(required=True, validate=validate.OneOf(["bookshelf", "desk", "box", "frame", "plant", "lamp"]))
    skin_id = fields.String(validate=validate.Length(max=32))
    grid_x = fields.Integer(required=True, validate=validate.Range(min=0, max=99))
    grid_y = fields.Integer(required=True, validate=validate.Range(min=0, max=99))
    z_index = fields.Integer(load_default=0)

class ItemUpdateSchema(BaseSchema):
    """PATCH /palace/items/{id}（PLS-05）：移动 / 重命名。"""
    grid_x = fields.Integer(validate=validate.Range(min=0, max=99))
    grid_y = fields.Integer(validate=validate.Range(min=0, max=99))
    name = fields.String(validate=validate.Length(max=64))

class ItemDeleteQuerySchema(BaseSchema):
    """DELETE /palace/items/{id}（PLS-05）：无入参（前端二次确认）。"""

class LinkSchema(BaseSchema):
    """POST /palace/items/{id}/link（PLS-03）：链接文件/笔记/错题。"""
    link_type = fields.String(required=True, validate=validate.OneOf(["file", "note", "wrong"]))
    link_id = fields.Integer(required=True, validate=validate.Range(min=1))

class ReviewQuerySchema(BaseSchema):
    """POST /palace/items/{id}/review（PLS-04）：无入参。"""

class ItemListQuerySchema(BaseSchema):
    """GET /palace/items（PLS-05）：无入参。"""

class RewardListQuerySchema(BaseSchema):
    """GET /palace/rewards（PLS-06）：无入参。"""

class RoomUpdateSchema(BaseSchema):
    """PATCH /palace/room（PLS-07）：主题切换。"""
    theme = fields.String(required=True, validate=validate.OneOf(["library", "japanese", "cyber", "forest"]))

"""palace 数据访问层声明：函数签名 + 查询目标，业务待团队实现。

约定：每个查询都必须带 user_id 过滤；禁止跨模块查表；事务在 service 层提交。
"""


def get_or_create_room(user_id):
    """查/插入 palace_room（user_id 唯一）；必须带 user_id。（PLS-01）"""
    raise NotImplementedError("palace.get_or_create_room 待实现（PLS-01）")

def create_palace_item(user_id, payload):
    """插入 palace_item（room 归属校验）；必须带 user_id。（PLS-02）"""
    raise NotImplementedError("palace.create_palace_item 待实现（PLS-02）")

def update_palace_item(user_id, item_id, payload):
    """更新 palace_item 坐标/名称；必须带 user_id。（PLS-05）"""
    raise NotImplementedError("palace.update_palace_item 待实现（PLS-05）")

def delete_palace_item(user_id, item_id):
    """删除 palace_item；必须带 user_id，不级联删源内容。（PLS-05）"""
    raise NotImplementedError("palace.delete_palace_item 待实现（PLS-05）")

def link_palace_item(user_id, item_id, payload):
    """更新 palace_item.link_type/link_id/name；必须带 user_id，跨模块内容按 id 校验归属（不 JOIN 别的模块表）。（PLS-03）"""
    raise NotImplementedError("palace.link_palace_item 待实现（PLS-03）")

def record_item_review(user_id, item_id, payload):
    """更新 palace_item.review_count/last_review_at；必须带 user_id。（PLS-04）"""
    raise NotImplementedError("palace.record_item_review 待实现（PLS-04）")

def list_palace_items(user_id):
    """查 palace_item（room + user_id）。（PLS-05）"""
    raise NotImplementedError("palace.list_palace_items 待实现（PLS-05）")

def list_palace_rewards(user_id):
    """查 palace_item（is_reward=true + user_id）。（PLS-06）"""
    raise NotImplementedError("palace.list_palace_rewards 待实现（PLS-06）")

def update_room_theme(user_id, payload):
    """更新 palace_room.theme；必须带 user_id。（PLS-07）"""
    raise NotImplementedError("palace.update_room_theme 待实现（PLS-07）")

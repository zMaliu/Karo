"""palace 计划数据表（框架不建表：本文件当前没有 Model 类，db.create_all() 也不会建表）。

团队实现时：按下面的字段要点写 db.Model，并启用 app/__init__.py 中被注释掉的建表代码。
"""

# 计划表（规格书 §6 + PRD 数据模型）：
# - palace_room：id、user_id(唯一 FK)、theme(默认 library)、width/height、created_at/updated_at
# - palace_item：id、room_id(FK)、item_type(bookshelf/desk/box/frame/plant/lamp)、skin_id、grid_x/grid_y/z_index、link_type(file/note/wrong/none)、link_id、name、is_reward、review_count、last_review_at、created_at/updated_at
# - palace_skin：id、skin_id(唯一)、item_type、image_url、unlock_condition、created_at/updated_at

"""twin 计划数据表（框架不建表：本文件当前没有 Model 类，db.create_all() 也不会建表）。

团队实现时：按下面的字段要点写 db.Model，并启用 app/__init__.py 中被注释掉的建表代码。
"""

# 计划表（规格书 §3 + PRD 数据模型）：
# - twin_profile：id、user_id(唯一 FK)、avatar_id、personality/catchphrases/weakness(JSON)、emotion、intimacy、mood_today、created_at/updated_at
# - twin_message：id、user_id(索引)、role(user/assistant)、content、emotion、created_at
# - twin_memory：id、user_id(索引)、content、embedding_id、importance、created_at

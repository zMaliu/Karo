"""account 计划数据表（框架不建表：本文件当前没有 Model 类，db.create_all() 也不会建表）。

团队实现时：按下面的字段要点写 db.Model，并启用 app/__init__.py 中被注释掉的建表代码。
"""

# 计划表（规格书 §1 + PRD 数据模型）：
# - user_account：id、phone(唯一索引)、nickname、avatar_url、grade、major、goal、status、last_login_at、created_at/updated_at
# - user_profile：id、user_id(唯一 FK)、personality/habits/aesthetic/weakness/emotion_tendency(JSON)、questionnaire_version、completed_at、show_online/personalized_rec/push_enabled

"""timer 计划数据表（框架不建表：本文件当前没有 Model 类，db.create_all() 也不会建表）。

团队实现时：按下面的字段要点写 db.Model，并启用 app/__init__.py 中被注释掉的建表代码。
"""

# 计划表（规格书 §2 + PRD 数据模型）：
# - timer_session：id、user_id(索引)、mode、subject_tag、status(ongoing/paused/completed/aborted)、start_at、end_at、paused_at、paused_sec、duration_sec、interrupted、interrupt_count、created_at/updated_at
# - timer_checkin：id、user_id、checkin_date(唯一 user+date)、streak、total_days、created_at/updated_at

"""solve 计划数据表（框架不建表：本文件当前没有 Model 类，db.create_all() 也不会建表）。

团队实现时：按下面的字段要点写 db.Model，并启用 app/__init__.py 中被注释掉的建表代码。
"""

# 计划表（规格书 §5 + PRD 数据模型）：
# - solve_session：id、user_id(索引)、subject_tag、source(photo/manual)、question_text、image_url、solution_steps(JSON)、final_answer、knowledge_tags(JSON)、model、status(solved/failed)、created_at/updated_at
# - wrong_question：id、user_id(索引)、session_id(FK)、question_text、answer、knowledge_tags(JSON)、wrong_reason、review_status(new/reviewed/mastered)、reviewed_at、created_at/updated_at

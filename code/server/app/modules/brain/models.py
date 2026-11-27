"""brain 计划数据表（框架不建表：本文件当前没有 Model 类，db.create_all() 也不会建表）。

团队实现时：按下面的字段要点写 db.Model，并启用 app/__init__.py 中被注释掉的建表代码。
"""

# 计划表（规格书 §4 + PRD 数据模型）：
# - brain_file：id、user_id(索引)、title、file_type(pdf/image/word/txt)、oss_url、hash(去重)、subject_tag、parse_status(parsing/ok/failed)、summary、created_at/updated_at
# - brain_note：id、user_id(索引)、title、content_md、tags(JSON)、created_at/updated_at
# - brain_diary：id、user_id(索引)、entry_date、mood、content、created_at/updated_at
# - brain_chunk：id、user_id(索引)、source_type(file/note/diary)、source_id、content、embedding_id、created_at

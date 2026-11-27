"""brain 数据访问层声明：函数签名 + 查询目标，业务待团队实现。

约定：每个查询都必须带 user_id 过滤；禁止跨模块查表；事务在 service 层提交。
"""


def create_brain_file(user_id, payload):
    """插入 brain_file；必须带 user_id；按 hash 去重。（BRN-01）"""
    raise NotImplementedError("brain.create_brain_file 待实现（BRN-01）")

def list_brain_files(user_id, params):
    """查 brain_file（user_id + 过滤条件 + 分页）；必须带 user_id。（BRN-05）"""
    raise NotImplementedError("brain.list_brain_files 待实现（BRN-05）")

def get_brain_file(user_id, file_id):
    """查 brain_file 主键 + user_id（越权 404）。（BRN-01）"""
    raise NotImplementedError("brain.get_brain_file 待实现（BRN-01）")

def create_brain_note(user_id, payload):
    """插入 brain_note；必须带 user_id。（BRN-02）"""
    raise NotImplementedError("brain.create_brain_note 待实现（BRN-02）")

def get_brain_note(user_id, note_id):
    """查 brain_note 主键 + user_id。（BRN-02）"""
    raise NotImplementedError("brain.get_brain_note 待实现（BRN-02）")

def update_brain_note(user_id, note_id, payload):
    """更新 brain_note；必须带 user_id。（BRN-06）"""
    raise NotImplementedError("brain.update_brain_note 待实现（BRN-06）")

def create_brain_diary(user_id, payload):
    """插入 brain_diary；必须带 user_id。（BRN-03）"""
    raise NotImplementedError("brain.create_brain_diary 待实现（BRN-03）")

def list_brain_diaries(user_id, params):
    """查 brain_diary（user_id + 日期范围 + 分页）。（BRN-03）"""
    raise NotImplementedError("brain.list_brain_diaries 待实现（BRN-03）")

def search_brain_chunks(user_id, payload):
    """检索 brain_chunk（user_id + 向量相似度 Top-K）；必须带 user_id。（BRN-04）"""
    raise NotImplementedError("brain.search_brain_chunks 待实现（BRN-04）")

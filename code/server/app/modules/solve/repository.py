"""solve 数据访问层声明：函数签名 + 查询目标，业务待团队实现。

约定：每个查询都必须带 user_id 过滤；禁止跨模块查表；事务在 service 层提交。
"""


def create_ocr_task(user_id, payload):
    """记录 OCR 任务（image_url/user_id）；必须带 user_id。（SLV-01）"""
    raise NotImplementedError("solve.create_ocr_task 待实现（SLV-01）")

def create_solve_session(user_id, payload):
    """插入 solve_session；必须带 user_id。（SLV-03）"""
    raise NotImplementedError("solve.create_solve_session 待实现（SLV-03）")

def get_solve_session(user_id, session_id):
    """查 solve_session 主键 + user_id。（SLV-03）"""
    raise NotImplementedError("solve.get_solve_session 待实现（SLV-03）")

def list_solve_sessions(user_id, params):
    """查 solve_session（user_id + 分页）；必须带 user_id。（SLV-06）"""
    raise NotImplementedError("solve.list_solve_sessions 待实现（SLV-06）")

def create_wrong_question(user_id, payload):
    """插入 wrong_question；必须带 user_id + 校验 session 归属。（SLV-04）"""
    raise NotImplementedError("solve.create_wrong_question 待实现（SLV-04）")

def list_wrong_questions(user_id, params):
    """查 wrong_question（user_id + 筛选）；必须带 user_id。（SLV-05）"""
    raise NotImplementedError("solve.list_wrong_questions 待实现（SLV-05）")

def update_wrong_question(user_id, wrong_id, payload):
    """更新 wrong_question；必须带 user_id。（SLV-05）"""
    raise NotImplementedError("solve.update_wrong_question 待实现（SLV-05）")

def delete_wrong_question(user_id, wrong_id):
    """删除 wrong_question；必须带 user_id。（SLV-05）"""
    raise NotImplementedError("solve.delete_wrong_question 待实现（SLV-05）")

def get_solve_hint(user_id, payload):
    """查 solve_session + 提示状态（user_id）。（SLV-07）"""
    raise NotImplementedError("solve.get_solve_hint 待实现（SLV-07）")

def list_variant_questions(user_id, payload):
    """按知识点查变式题池（user_id 归属校验）。（SLV-08）"""
    raise NotImplementedError("solve.list_variant_questions 待实现（SLV-08）")

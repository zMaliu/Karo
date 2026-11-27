"""solve 服务层声明：函数签名 + 实现步骤要点，业务待团队实现（规格书 §5）。

当前所有函数体只有 raise NotImplementedError（路由暂未调用），
由 app/common/errors.py 的 NotImplementedError handler 统一转 501。
"""


def ocr(user_id, payload):
    """SLV-01：拍照 OCR 识题。

    实现步骤：
    1. 校验图片 ≤10MB 且格式合法。
    2. 调用 OCR 得到题目文本并返回可编辑预览；低置信度段落标红。
    3. OCR 失败提示重拍，可改手动录入。
    """
    raise NotImplementedError("solve.ocr 待实现（SLV-01）")

def create_session(user_id, payload):
    """SLV-03：提交求解（流式）。

    实现步骤：
    1. 校验题干预非空 ≤2000 字、source 合法。
    2. 组装解题 Prompt → 流式推理 → 结构化解析（步骤/答案/知识点）。
    3. 写 solve_session(status=solved/failed)；不确定答案标注「需核对」。
    """
    raise NotImplementedError("solve.create_session 待实现（SLV-03）")

def get_session(user_id, session_id):
    """SLV-03：解题结果。

    实现步骤：
    1. 按 user_id + id 查 solve_session，越权 404。
    2. 返回分步过程/最终答案/知识点标签/状态。
    """
    raise NotImplementedError("solve.get_session 待实现（SLV-03）")

def list_sessions(user_id, params):
    """SLV-06：解题历史。

    实现步骤：
    1. 按 user_id + 可选科目查解题历史。
    2. 按 created_at 倒序分页。
    """
    raise NotImplementedError("solve.list_sessions 待实现（SLV-06）")

def create_wrong(user_id, payload):
    """SLV-04：一键收入错题本。

    实现步骤：
    1. 校验会话归属；同题重复收录返回 409。
    2. 写 wrong_question 并关联知识点标签；错因可后补。
    """
    raise NotImplementedError("solve.create_wrong 待实现（SLV-04）")

def list_wrongs(user_id, params):
    """SLV-05：错题筛选 / 重做。

    实现步骤：
    1. 按 user_id + 科目/复习状态筛选错题。
    2. 返回 items（题干/标签/错因/复习状态）。
    """
    raise NotImplementedError("solve.list_wrongs 待实现（SLV-05）")

def update_wrong(user_id, wrong_id, payload):
    """SLV-05：补错因 / 标记掌握。

    实现步骤：
    1. 按 user_id + id 查错题，越权 404。
    2. 更新错因/复习状态；标记 mastered 时记录 reviewed_at。
    """
    raise NotImplementedError("solve.update_wrong 待实现（SLV-05）")

def delete_wrong(user_id, wrong_id):
    """SLV-05：删除错题。

    实现步骤：
    1. 按 user_id + id 校验归属。
    2. 删除错题，不影响 brain 中其他资料。
    """
    raise NotImplementedError("solve.delete_wrong 待实现（SLV-05）")

def hints(user_id, payload):
    """SLV-07：引导式分步求解。

    实现步骤：
    1. 按 user_id 校验会话归属。
    2. 按卡点返回下一层提示（≤20 字），不直接给全解。
    3. 最后一步才返回完整过程；V0.1 结果页保留「换种讲法」入口。
    """
    raise NotImplementedError("solve.hints 待实现（SLV-07）")

def variants(user_id, payload):
    """SLV-08：变式题推荐。

    实现步骤：
    1. 按错题知识点匹配同类变式题（V0.5 实现）。
    2. 按复习曲线安排推送；本期返回空数组占位。
    """
    raise NotImplementedError("solve.variants 待实现（SLV-08）")

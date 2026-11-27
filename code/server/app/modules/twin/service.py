"""twin 服务层声明：函数签名 + 实现步骤要点，业务待团队实现（规格书 §3）。

当前所有函数体只有 raise NotImplementedError（路由暂未调用），
由 app/common/errors.py 的 NotImplementedError handler 统一转 501。
"""


def select_avatar(user_id, payload):
    """TWN-02：形象选择。

    实现步骤：
    1. 校验 avatar_id 属于 3 个预设形象。
    2. upsert twin_profile.avatar_id；未选时按审美偏好默认分配。
    3. 返回学伴配置（形象/头像地址等）。
    """
    raise NotImplementedError("twin.select_avatar 待实现（TWN-02）")

def get_profile(user_id):
    """TWN-07：亲密度 / 学伴资料。

    实现步骤：
    1. 按 user_id 查 twin_profile。
    2. 返回画像标签/亲密度/等级/形象；无记录时返回默认空态。
    """
    raise NotImplementedError("twin.get_profile 待实现（TWN-07）")

def list_messages(user_id, params):
    """TWN-08：历史会话。

    实现步骤：
    1. 按 user_id 查 twin_message，before_id 做游标分页。
    2. 按 created_at/id 倒序返回 items 与 next_before_id。
    """
    raise NotImplementedError("twin.list_messages 待实现（TWN-08）")

def send_message(user_id, payload):
    """TWN-03：流式对话。

    实现步骤：
    1. 校验 content 非空且 ≤500 字，落库 role=user。
    2. 情绪识别 + 长期记忆召回（近 10 轮短期记忆；召回为空不拼记忆）。
    3. 组装 Prompt 调 LLM 并在内容审核通过后流式返回。
    4. 审核拦截返回安全提示；流式中断可重发。
    """
    raise NotImplementedError("twin.send_message 待实现（TWN-03）")

def search_memory(user_id, payload):
    """TWN-04：长期记忆检索。

    实现步骤：
    1. 把 query 向量化并对本人记忆做 Top-K 召回。
    2. 去重后返回相关片段；召回为空返回空数组，不编造历史。
    """
    raise NotImplementedError("twin.search_memory 待实现（TWN-04）")

def list_proactive(user_id):
    """TWN-06：主动消息列表。

    实现步骤：
    1. 查已下发的主动消息（冷却/日上限由规则保证）。
    2. 夜间静默、用户可关闭；返回 items。
    """
    raise NotImplementedError("twin.list_proactive 待实现（TWN-06）")

def add_intimacy(user_id, payload):
    """TWN-07：亲密度事件上报。

    实现步骤：
    1. 按事件类型累加亲密度（只增不减）。
    2. 达到阈值升级并返回 level；同一事件去重。
    """
    raise NotImplementedError("twin.add_intimacy 待实现（TWN-07）")

def get_mood(user_id):
    """TWN-05：当前情绪状态。

    实现步骤：
    1. 读最近一次情绪识别结果（twin_profile.emotion/mood_today）。
    2. 低置信度按平静处理，返回情绪与建议语气。
    """
    raise NotImplementedError("twin.get_mood 待实现（TWN-05）")

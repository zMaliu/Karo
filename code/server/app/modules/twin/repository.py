"""twin 数据访问层声明：函数签名 + 查询目标，业务待团队实现。

约定：每个查询都必须带 user_id 过滤；禁止跨模块查表；事务在 service 层提交。
"""


def upsert_twin_profile(user_id, payload):
    """upsert twin_profile.avatar_id；必须带 user_id。（TWN-02）"""
    raise NotImplementedError("twin.upsert_twin_profile 待实现（TWN-02）")

def get_twin_profile(user_id):
    """查 twin_profile.user_id；必须带 user_id。（TWN-07）"""
    raise NotImplementedError("twin.get_twin_profile 待实现（TWN-07）")

def list_twin_messages(user_id, params):
    """查 twin_message（user_id + before_id 游标排序）；必须带 user_id。（TWN-08）"""
    raise NotImplementedError("twin.list_twin_messages 待实现（TWN-08）")

def save_twin_message(user_id, payload):
    """写 twin_message（user/assistant 两条）；必须带 user_id。（TWN-03）"""
    raise NotImplementedError("twin.save_twin_message 待实现（TWN-03）")

def search_twin_memory(user_id, payload):
    """查 twin_memory（user_id + 向量相似度）；必须带 user_id。（TWN-04）"""
    raise NotImplementedError("twin.search_twin_memory 待实现（TWN-04）")

def list_proactive_messages(user_id):
    """查 twin 主动消息（user_id + 时段）；必须带 user_id。（TWN-06）"""
    raise NotImplementedError("twin.list_proactive_messages 待实现（TWN-06）")

def add_intimacy(user_id, payload):
    """更新 twin_profile.intimacy；必须带 user_id，只增不减。（TWN-07）"""
    raise NotImplementedError("twin.add_intimacy 待实现（TWN-07）")

def get_twin_mood(user_id):
    """查 twin_profile.emotion/mood_today；必须带 user_id。（TWN-05）"""
    raise NotImplementedError("twin.get_twin_mood 待实现（TWN-05）")

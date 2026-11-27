"""account 数据访问层声明：函数签名 + 查询目标，业务待团队实现。

约定：每个查询都必须带 user_id 过滤；禁止跨模块查表；事务在 service 层提交。
"""


def save_otp_code(payload):
    """暂不落库：后续接短信通道/缓存；禁止跨模块查表。（ACC-01）"""
    raise NotImplementedError("account.save_otp_code 待实现（ACC-01）")

def get_user_by_phone(payload):
    """查 user_account.phone（唯一索引）；登录入口，无需 user_id 过滤。（ACC-01）"""
    raise NotImplementedError("account.get_user_by_phone 待实现（ACC-01）")

def get_user_by_id(user_id):
    """查 user_account 主键；必须按 user_id 过滤，禁止查他人。（ACC-03）"""
    raise NotImplementedError("account.get_user_by_id 待实现（ACC-03）")

def update_user(user_id, payload):
    """更新 user_account 白名单字段；必须带 user_id 条件。（ACC-03）"""
    raise NotImplementedError("account.update_user 待实现（ACC-03）")

def get_profile_by_user(user_id):
    """查 user_profile.user_id（唯一）；必须按 user_id 过滤。（ACC-06）"""
    raise NotImplementedError("account.get_profile_by_user 待实现（ACC-06）")

def update_privacy(user_id, payload):
    """更新 user_profile 隐私字段；必须带 user_id。（ACC-06）"""
    raise NotImplementedError("account.update_privacy 待实现（ACC-06）")

def save_questionnaire(user_id, payload):
    """更新 user_profile 画像 JSON 字段；必须带 user_id，保留历史版本。（ACC-04）"""
    raise NotImplementedError("account.save_questionnaire 待实现（ACC-04）")

def list_devices(user_id):
    """查登录设备记录（本期可只返回当前设备）；必须按 user_id 过滤。（ACC-07）"""
    raise NotImplementedError("account.list_devices 待实现（ACC-07）")

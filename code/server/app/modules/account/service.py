"""account 服务层声明：函数签名 + 实现步骤要点，业务待团队实现（规格书 §1）。

当前所有函数体只有 raise NotImplementedError（路由暂未调用），
由 app/common/errors.py 的 NotImplementedError handler 统一转 501。
"""


def send_otp(payload):
    """ACC-01：发送验证码。

    实现步骤：
    1. 校验手机号格式（11 位、1[3-9] 开头），不合法返回 422。
    2. 生成 6 位验证码并投递短信通道；dev 模式把 code 也回传为 dev_code。
    3. 60 秒内重复发送返回 429 OTP_TOO_FREQUENT，正常返回 expires_in=300。
    """
    raise NotImplementedError("account.send_otp 待实现（ACC-01）")

def login(payload):
    """ACC-01：登录 / 自动建档。

    实现步骤：
    1. 校验 phone/code 与验证码有效期，错误返回 400 OTP_INVALID。
    2. 按 phone 查 user_account，不存在则自动建档并初始化 user_profile（is_new=true）。
    3. 签发 JWT（sub=user_id，7 天），更新 last_login_at，返回 access_token/is_new/user。
    """
    raise NotImplementedError("account.login 待实现（ACC-01）")

def get_me(user_id):
    """ACC-03：我的账号资料。

    实现步骤：
    1. 从 g.user_id 取当前用户，不信任任何入参。
    2. 查 user_account，status 非 active 返回 401。
    3. 返回 id/phone/nickname/avatar_url/grade/major/goal/status/时间字段。
    """
    raise NotImplementedError("account.get_me 待实现（ACC-03）")

def update_me(user_id, payload):
    """ACC-03：修改资料。

    实现步骤：
    1. 按 g.user_id 查 user_account，不存在返回 404。
    2. 只更新白名单字段（昵称 ≤20、头像 ≤255、年级 ≤16、专业 ≤32、目标 ≤128）。
    3. commit 后返回更新后的 user。
    """
    raise NotImplementedError("account.update_me 待实现（ACC-03）")

def get_profile(user_id):
    """ACC-06：画像标签 + 隐私开关。

    实现步骤：
    1. 按 g.user_id 查 user_profile（与 user_account 1:1）。
    2. 把画像 JSON 标签与隐私开关合并为 data。
    3. 未完成问卷时标签返回空数组，并带 questionnaire_version/completed_at。
    """
    raise NotImplementedError("account.get_profile 待实现（ACC-06）")

def update_privacy(user_id, payload):
    """ACC-06：更新隐私偏好。

    实现步骤：
    1. 至少传一个开关，否则 422。
    2. 按 g.user_id 更新 user_profile 的三个布尔列（隐私表按 4 表约束并入 user_profile）。
    3. 返回生效后的 privacy 对象。
    """
    raise NotImplementedError("account.update_privacy 待实现（ACC-06）")

def submit_questionnaire(user_id, payload):
    """ACC-04：提交 / 重测 25 题问卷。

    实现步骤：
    1. 校验 answers 恰好 25 题且选项合法。
    2. 按题号映射到 personality/habits/aesthetic/weakness/emotion_tendency 标签。
    3. 写 user_profile 并更新 questionnaire_version/completed_at；重测保留旧版本。
    """
    raise NotImplementedError("account.submit_questionnaire 待实现（ACC-04）")

def list_devices(user_id):
    """ACC-07：登录设备列表。

    实现步骤：
    1. 按 g.user_id 查登录设备/会话记录（V0.1 可先只返回当前设备）。
    2. 返回 items；后续支持踢下线。
    """
    raise NotImplementedError("account.list_devices 待实现（ACC-07）")

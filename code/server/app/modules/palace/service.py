"""palace 服务层声明：函数签名 + 实现步骤要点，业务待团队实现（规格书 §6）。

当前所有函数体只有 raise NotImplementedError（路由暂未调用），
由 app/common/errors.py 的 NotImplementedError handler 统一转 501。
"""


def get_room(user_id):
    """PLS-01：房间初始化 / 读取。

    实现步骤：
    1. 按 user_id 查 palace_room；无则创建默认房间（主题 library + 书架/书桌各 1）。
    2. 重复进入不重复创建；返回 room + items。
    """
    raise NotImplementedError("palace.get_room 待实现（PLS-01）")

def create_item(user_id, payload):
    """PLS-02：摆放物品。

    实现步骤：
    1. 校验槽位上限 20；目标格被占用则推荐最近空位。
    2. 写 palace_item（link_type=none 的空物品可先摆放）。
    3. 返回物品与最终坐标。
    """
    raise NotImplementedError("palace.create_item 待实现（PLS-02）")

def update_item(user_id, item_id, payload):
    """PLS-05：移动 / 重命名物品。

    实现步骤：
    1. 按 user_id + id 查物品，越权 404。
    2. 更新坐标或名称；坐标占用同样做避让校验。
    """
    raise NotImplementedError("palace.update_item 待实现（PLS-05）")

def delete_item(user_id, item_id):
    """PLS-05：删除物品。

    实现步骤：
    1. 按 user_id + id 校验归属；删除物品不删大脑源文件。
    2. 删除后释放槽位。
    """
    raise NotImplementedError("palace.delete_item 待实现（PLS-05）")

def link_item(user_id, item_id, payload):
    """PLS-03：链接文件 / 笔记 / 错题。

    实现步骤：
    1. 校验 item 归属与目标内容归属（调 brain/solve 的 service）。
    2. 一个物品只链一份内容；回填 name 为内容标题。
    3. 内容不存在返回 404，已失效物品提示重新链接。
    """
    raise NotImplementedError("palace.link_item 待实现（PLS-03）")

def review_item(user_id, item_id, payload):
    """PLS-04：点击复习并记录。

    实现步骤：
    1. 按 user_id + id 查物品；空物品无打开入口。
    2. review_count += 1、last_review_at=now；失效内容只提示不可打开。
    """
    raise NotImplementedError("palace.review_item 待实现（PLS-04）")

def list_items(user_id):
    """PLS-05：物品管理列表。

    实现步骤：
    1. 按 room 查全部物品，返回网格坐标/链接状态/复习统计。
    """
    raise NotImplementedError("palace.list_items 待实现（PLS-05）")

def list_rewards(user_id):
    """PLS-06：奖励物品列表。

    实现步骤：
    1. 返回已发放奖励物品；同一成就不重复发放。
    2. 奖励物品不可被普通删除（is_reward 标记）。
    """
    raise NotImplementedError("palace.list_rewards 待实现（PLS-06）")

def update_theme(user_id, payload):
    """PLS-07：主题切换。

    实现步骤：
    1. 校验主题解锁状态（V0.1 仅 library，其余置灰）。
    2. 切换背景与物品皮肤风格；资源失败保持原主题。
    """
    raise NotImplementedError("palace.update_theme 待实现（PLS-07）")

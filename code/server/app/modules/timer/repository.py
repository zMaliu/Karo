"""timer 数据访问层声明：函数签名 + 查询目标，业务待团队实现。

约定：每个查询都必须带 user_id 过滤；禁止跨模块查表；事务在 service 层提交。
"""


def create_timer_session(user_id, payload):
    """插入 timer_session；user_id 来自 JWT。（TMR-01）"""
    raise NotImplementedError("timer.create_timer_session 待实现（TMR-01）")

def get_timer_session(user_id, session_id, payload):
    """按 id + user_id 查 timer_session（越权 404）。（TMR-01）"""
    raise NotImplementedError("timer.get_timer_session 待实现（TMR-01）")

def save_timer_settlement(user_id, session_id, payload):
    """更新 timer_session 结算字段 + upsert timer_checkin；必须带 user_id，按自然日聚合。（TMR-07）"""
    raise NotImplementedError("timer.save_timer_settlement 待实现（TMR-07）")

def abort_timer_session(user_id, session_id, payload):
    """更新 timer_session.status=aborted；必须带 user_id。（TMR-01）"""
    raise NotImplementedError("timer.abort_timer_session 待实现（TMR-01）")

def get_active_timer_session(user_id):
    """查 timer_session（user_id + status in ongoing/paused），按 id desc 取 1 条。（TMR-08）"""
    raise NotImplementedError("timer.get_active_timer_session 待实现（TMR-08）")

def list_timer_sessions(user_id, params):
    """查 timer_session 最近 N 条；必须带 user_id + 排序。（TMR-08）"""
    raise NotImplementedError("timer.list_timer_sessions 待实现（TMR-08）")

def aggregate_timer_stats(user_id, params):
    """聚合 timer_session（user_id + 时间窗口）与 timer_checkin；只读聚合且必须带 user_id。（TMR-08）"""
    raise NotImplementedError("timer.aggregate_timer_stats 待实现（TMR-08）")

def increment_interrupt(user_id, session_id, payload):
    """更新 timer_session.interrupt_count/interrupted；必须带 user_id。（TMR-05）"""
    raise NotImplementedError("timer.increment_interrupt 待实现（TMR-05）")

def aggregate_month_stats(user_id, params):
    """聚合 timer_session 月窗口；必须带 user_id。（TMR-08）"""
    raise NotImplementedError("timer.aggregate_month_stats 待实现（TMR-08）")

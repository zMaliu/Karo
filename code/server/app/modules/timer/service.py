"""timer 服务层声明：函数签名 + 实现步骤要点，业务待团队实现（规格书 §2）。

当前所有函数体只有 raise NotImplementedError（路由暂未调用），
由 app/common/errors.py 的 NotImplementedError handler 统一转 501。
"""


def create_session(user_id, payload):
    """TMR-01：开始专注。

    实现步骤：
    1. 校验 mode 属于三种模式；已存在进行中会话返回 409 SESSION_ACTIVE。
    2. 写 timer_session（status=ongoing、start_at=服务端 UTC 时间）。
    3. 返回 session（含 id/start_at/elapsed_sec=0）。
    """
    raise NotImplementedError("timer.create_session 待实现（TMR-01）")

def update_session(user_id, session_id, payload):
    """TMR-01：暂停 / 继续 / 心跳。

    实现步骤：
    1. 按 user_id + id 查会话，越权/不存在统一 404。
    2. pause 置 status=paused/paused_at；resume 累计 paused_sec 并回 ongoing；heartbeat 只刷新 updated_at。
    3. 状态非法返回 409 SESSION_STATE_INVALID；返回 session + server_time。
    """
    raise NotImplementedError("timer.update_session 待实现（TMR-01）")

def complete_session(user_id, session_id, payload):
    """TMR-07：完成专注（结算 + 连签，幂等）。

    实现步骤：
    1. 按 user_id + id 查会话；已 completed 直接回放结果（幂等）。
    2. 服务端结算 duration_sec = end - start - paused_sec，status=completed。
    3. 按 X-Client-Timezone 自然日写 timer_checkin（有效时长 ≥60s）并累加 streak。
    """
    raise NotImplementedError("timer.complete_session 待实现（TMR-07）")

def abort_session(user_id, session_id, payload):
    """TMR-01：放弃本次专注。

    实现步骤：
    1. 按 user_id + id 查会话，非进行中返回 409。
    2. 结算实际时长后置 status=aborted（不记签到）。
    """
    raise NotImplementedError("timer.abort_session 待实现（TMR-01）")

def active_session(user_id):
    """TMR-08：进行中会话（重启恢复）。

    实现步骤：
    1. 按 user_id 查 status ∈ {ongoing, paused} 的最新会话。
    2. 没有则返回 session=null（客户端据此回到未开始态）。
    """
    raise NotImplementedError("timer.active_session 待实现（TMR-08）")

def list_sessions(user_id, params):
    """TMR-08：专注历史。

    实现步骤：
    1. 按 user_id 取最近 N 条（默认 20，V0.1 不分页）。
    2. 按 start_at/id 倒序返回 items。
    """
    raise NotImplementedError("timer.list_sessions 待实现（TMR-08）")

def get_stats(user_id, params):
    """TMR-08：今日 / 本周统计。

    实现步骤：
    1. 按 X-Client-Timezone 把 today/week 窗口换算成 UTC 起止。
    2. 聚合 status=completed 的 duration_sec、会话数、有效会话数（≥60s）。
    3. 附带 streak/total_checkin_days 与 today/week 时长。
    """
    raise NotImplementedError("timer.get_stats 待实现（TMR-08）")

def report_interrupt(user_id, session_id, payload):
    """TMR-05：中断上报。

    实现步骤：
    1. 按 user_id + id 查进行中会话，否则 409。
    2. 累加 interrupt_count 并置 interrupted=true；同秒重复上报去抖。
    """
    raise NotImplementedError("timer.report_interrupt 待实现（TMR-05）")

def get_month_stats(user_id, params):
    """TMR-08：月度统计。

    实现步骤：
    1. 按月窗口换算 UTC 起止（时区取 X-Client-Timezone）。
    2. 复用 stats 聚合口径返回本月时长/会话数/签到。
    """
    raise NotImplementedError("timer.get_month_stats 待实现（TMR-08）")

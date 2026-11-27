# timer — 专注时钟

**负责人**：C ｜ **实现 Sprint**：W1-W2 ｜ **当前状态**：接口声明（9 个端点全部返回 501，业务待实现）

## 1. 职责
番茄/自由专注计时（倒计时为后续）：会话状态机、服务端结算有效时长、按客户端自然日签到与连签、今日/本周/月度统计。

## 2. 端点表（方法 / 路径 / 功能编号 / 负责人 / Sprint / 规格书章节）
| 方法 | 路径 | 功能编号 | 负责人 | Sprint | 规格书 |
|---|---|---|---|---|---|
| POST | `/api/v1/timer/sessions` | TMR-01 | C | W1 | §2 TMR-01 |
| PATCH | `/api/v1/timer/sessions/{id}` | TMR-01 | C | W1 | §2 TMR-01 |
| POST | `/api/v1/timer/sessions/{id}/complete` | TMR-07 | C | W1 | §2 TMR-07 |
| POST | `/api/v1/timer/sessions/{id}/abort` | TMR-01 | C | W1 | §2 TMR-01 |
| GET | `/api/v1/timer/sessions/active` | TMR-08 | C | W1 | §2 TMR-08 |
| GET | `/api/v1/timer/sessions` | TMR-08 | C | W1 | §2 TMR-08 |
| GET | `/api/v1/timer/stats` | TMR-08 | C | W1 | §2 TMR-08 |
| POST | `/api/v1/timer/sessions/{id}/interrupt` | TMR-05 | C | W2 | §2 TMR-05 |
| GET | `/api/v1/timer/stats/month` | TMR-08 | C | W2 | §2 TMR-08 |

所有路径前缀都是 `/api/v1`；完整契约见 `contracts/api.md`，功能逻辑见 `功能实现规格书.md` §2。

## 3. 计划数据表（只写在 models.py 注释里，框架启动不建表）
- timer_session：id、user_id(索引)、mode、subject_tag、status(ongoing/paused/completed/aborted)、start_at、end_at、paused_at、paused_sec、duration_sec、interrupted、interrupt_count、created_at/updated_at
- timer_checkin：id、user_id、checkin_date(唯一 user+date)、streak、total_days、created_at/updated_at

## 4. 依赖的其他模块
- 身份/鉴权：JWT 由 account 签发，g.user_id 由 app/common/auth.py 注入。
- 时区：X-Client-Timezone 决定自然日与统计窗口，缺一不可。
- 对外提供 GET /timer/stats 给 twin 生成鼓励/催促语。

## 5. 实现步骤
1. 读 `功能实现规格书.md` §2 中本模块各功能条目（逻辑流程 / 数据变化 / 边界与异常 / 验收）。
2. 在 `schemas.py` 用已声明的 Schema 校验入参（`routes.py` 中 `.load()`），非法 → 422 且不落库。
3. 在 `service.py` 实现函数体（替换 `raise NotImplementedError`），按 docstring 步骤逐条落。
4. 在 `repository.py` 写查询（必须带 user_id）并在 `models.py` 建 Model，然后启用建表。
5. 把 `routes.py` 里的 `_todo(...)` 换成「校验 + 调 service + `success(...)`」，补 pytest 并用 curl 自测。
6. 结算与连签全部用服务端时间；完成接口必须幂等；越权统一 404。

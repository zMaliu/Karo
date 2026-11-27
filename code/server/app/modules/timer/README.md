# timer — 专注时钟

负责人：C ｜ 分支：`backend-b` ｜ 接口：9 个（全部 501，待实现）

- 职责：番茄/自由专注计时、暂停恢复、中断记录、完成结算、按客户端自然日连签、历史与统计。
- 功能：TMR-01/02/04/05/07/08（规格书 §2）
- 数据表：timer_session、timer_checkin（DDL 见 `server/schema.sql`）
- 依赖：依赖 account 的 JWT；行为数据本期只在模块内使用（跨模块聚合等 LOS）。
- 开始写：实现步骤见 `code/README.md` 的 5 步；接口见 `contracts/api.md`。
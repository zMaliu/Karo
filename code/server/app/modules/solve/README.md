# solve — AI 解题室

负责人：C ｜ 分支：`backend-b` ｜ 接口：10 个（全部 501，待实现）

- 职责：拍照 OCR、手动录入、AI 推理求解、一键错题、错题本管理。
- 功能：SLV-01/02/03/04/05（规格书 §5；历史/引导/变式后续）
- 数据表：solve_session、wrong_question（DDL 见 `server/schema.sql`）
- 依赖：依赖 account；错题提供给 palace 链接。
- 开始写：实现步骤见 `code/README.md` 的 5 步；接口见 `contracts/api.md`。
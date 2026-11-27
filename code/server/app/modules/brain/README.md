# brain — 智脑

负责人：B ｜ 分支：`backend-a` ｜ 接口：9 个（全部 501，待实现）

- 职责：文件上传与解析、Markdown 笔记、学习日记、文件筛选。
- 功能：BRN-01/02/03/05（规格书 §4；RAG/内容管理/图谱/卡片后续）
- 数据表：brain_file、brain_note、brain_diary、brain_chunk（DDL 见 `server/schema.sql`）
- 依赖：依赖 account；对外提供可链接内容给 palace。
- 开始写：实现步骤见 `code/README.md` 的 5 步；接口见 `contracts/api.md`。
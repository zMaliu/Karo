# twin — 数字孪生（学伴）

负责人：B ｜ 分支：`backend-a` ｜ 接口：8 个（全部 501，待实现）

- 职责：形象选择、流式对话（情绪+近 10 轮上下文）、情绪语气、亲密度、历史会话。
- 功能：TWN-02/03/05/07/08（规格书 §3；TWN-01 复用 ACC-04，其余后续）
- 数据表：twin_profile、twin_message（DDL 见 `server/schema.sql`）
- 依赖：读 account 画像生成人格；后续 RAG 读 brain 资料。
- 开始写：实现步骤见 `code/README.md` 的 5 步；接口见 `contracts/api.md`。
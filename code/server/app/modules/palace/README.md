# palace — 记忆宫殿

负责人：C ｜ 分支：`backend-b` ｜ 接口：9 个（全部 501，待实现）

- 职责：房间初始化、物品摆放、链接笔记/错题、点击复习、重命名/移动/删除。
- 功能：PLS-01~05（规格书 §6；奖励/主题/离线后续）
- 数据表：palace_room、palace_item、palace_skin（DDL 见 `server/schema.sql`）
- 依赖：依赖 account；链接内容只校验归属、存 link_type+link_id，不 JOIN 对方表。
- 开始写：实现步骤见 `code/README.md` 的 5 步；接口见 `contracts/api.md`。
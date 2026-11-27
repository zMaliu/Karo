# account — 账号与画像

负责人：B ｜ 分支：`backend-a` ｜ 接口：8 个（全部 501，待实现）

- 职责：身份底座：验证码登录/建档、资料、25 题画像问卷、隐私偏好；所有模块的 userId 都来自本模块签发的 JWT。
- 功能：ACC-01/03/04/05/06/07（规格书 §1）
- 数据表：user_account、user_profile、user_device（DDL 见 `server/schema.sql`）
- 依赖：无上游；对外提供 `/account/me`、`/account/profile` 给 twin/brain/palace。
- 开始写：实现步骤见 `code/README.md` 的 5 步；接口见 `contracts/api.md`。
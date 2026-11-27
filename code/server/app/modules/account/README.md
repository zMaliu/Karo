# account — 账号与画像

**负责人**：B ｜ **实现 Sprint**：W1-W2 ｜ **当前状态**：接口声明（8 个端点全部返回 501，业务待实现）

## 1. 职责
身份底座：手机号验证码登录/自动建档、基础资料维护、25 题画像问卷、隐私偏好。所有模块的 userId 都来自本模块签发的 JWT。

## 2. 端点表（方法 / 路径 / 功能编号 / 负责人 / Sprint / 规格书章节）
| 方法 | 路径 | 功能编号 | 负责人 | Sprint | 规格书 |
|---|---|---|---|---|---|
| POST | `/api/v1/account/otp/send` | ACC-01 | B | W1 | §1 ACC-01 |
| POST | `/api/v1/account/login` | ACC-01 | B | W1 | §1 ACC-01 |
| GET | `/api/v1/account/me` | ACC-03 | B | W1 | §1 ACC-03 |
| PATCH | `/api/v1/account/me` | ACC-03 | B | W1 | §1 ACC-03 |
| GET | `/api/v1/account/profile` | ACC-06 | B | W2 | §1 ACC-06 |
| PUT | `/api/v1/account/privacy` | ACC-06 | B | W2 | §1 ACC-06 |
| POST | `/api/v1/account/questionnaire` | ACC-04 | B | W2 | §1 ACC-04 |
| GET | `/api/v1/account/devices` | ACC-07 | B | W2 | §1 ACC-07 |

所有路径前缀都是 `/api/v1`；完整契约见 `contracts/api.md`，功能逻辑见 `功能实现规格书.md` §1。

## 3. 计划数据表（只写在 models.py 注释里，框架启动不建表）
- user_account：id、phone(唯一索引)、nickname、avatar_url、grade、major、goal、status、last_login_at、created_at/updated_at
- user_profile：id、user_id(唯一 FK)、personality/habits/aesthetic/weakness/emotion_tendency(JSON)、questionnaire_version、completed_at、show_online/personalized_rec/push_enabled

## 4. 依赖的其他模块
- 无上游依赖；短信通道由 B 自接，dev 模式直接回显 dev_code。
- 对外提供 GET /account/me、GET /account/profile 给 twin/brain/palace 读身份与画像；JWT 是所有模块的鉴权来源。

## 5. 实现步骤
1. 读 `功能实现规格书.md` §1 中本模块各功能条目（逻辑流程 / 数据变化 / 边界与异常 / 验收）。
2. 在 `schemas.py` 用已声明的 Schema 校验入参（`routes.py` 中 `.load()`），非法 → 422 且不落库。
3. 在 `service.py` 实现函数体（替换 `raise NotImplementedError`），按 docstring 步骤逐条落。
4. 在 `repository.py` 写查询（必须带 user_id）并在 `models.py` 建 Model，然后启用建表。
5. 把 `routes.py` 里的 `_todo(...)` 换成「校验 + 调 service + `success(...)`」，补 pytest 并用 curl 自测。
6. 隐私开关按 4 张表约束并入 user_profile；问卷重测要保留历史版本。

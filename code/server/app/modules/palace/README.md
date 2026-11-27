# palace — 记忆宫殿

**负责人**：C ｜ **实现 Sprint**：W4 ｜ **当前状态**：接口声明（9 个端点全部返回 501，业务待实现）

## 1. 职责
2.5D 房间内摆放物品，每个物品链接一份大脑文件/笔记/错题，把抽象资料变成空间化记忆锚点；支持移动、复习记录、奖励物品。本期只做默认主题 + 6 类基础物品。

## 2. 端点表（方法 / 路径 / 功能编号 / 负责人 / Sprint / 规格书章节）
| 方法 | 路径 | 功能编号 | 负责人 | Sprint | 规格书 |
|---|---|---|---|---|---|
| GET | `/api/v1/palace/room` | PLS-01 | C | W4 | §6 PLS-01 |
| POST | `/api/v1/palace/items` | PLS-02 | C | W4 | §6 PLS-02 |
| PATCH | `/api/v1/palace/items/{id}` | PLS-05 | C | W4 | §6 PLS-05 |
| DELETE | `/api/v1/palace/items/{id}` | PLS-05 | C | W4 | §6 PLS-05 |
| POST | `/api/v1/palace/items/{id}/link` | PLS-03 | C | W4 | §6 PLS-03 |
| POST | `/api/v1/palace/items/{id}/review` | PLS-04 | C | W4 | §6 PLS-04 |
| GET | `/api/v1/palace/items` | PLS-05 | C | W4 | §6 PLS-05 |
| GET | `/api/v1/palace/rewards` | PLS-06 | C | 后续 | 后续版本 |
| PATCH | `/api/v1/palace/room` | PLS-07 | C | 后续 | 后续版本 |

所有路径前缀都是 `/api/v1`；完整契约见 `contracts/api.md`，功能逻辑见 `功能实现规格书.md` §6。

## 3. 计划数据表（只写在 models.py 注释里，框架启动不建表）
- palace_room：id、user_id(唯一 FK)、theme(默认 library)、width/height、created_at/updated_at
- palace_item：id、room_id(FK)、item_type(bookshelf/desk/box/frame/plant/lamp)、skin_id、grid_x/grid_y/z_index、link_type(file/note/wrong/none)、link_id、name、is_reward、review_count、last_review_at、created_at/updated_at
- palace_skin：id、skin_id(唯一)、item_type、image_url、unlock_condition、created_at/updated_at

## 4. 依赖的其他模块
- 身份：JWT（account 签发）；房间与物品仅本人可见。
- B(brain)：GET /brain/files/{id}、GET /brain/notes/{id} 校验链接内容归属并回填物品名称。
- C(solve)：GET /solve/wrongs 取错题作为可链接内容；内容被删时物品置「已失效」灰态。

## 5. 实现步骤
1. 读 `功能实现规格书.md` §6 中本模块各功能条目（逻辑流程 / 数据变化 / 边界与异常 / 验收）。
2. 在 `schemas.py` 用已声明的 Schema 校验入参（`routes.py` 中 `.load()`），非法 → 422 且不落库。
3. 在 `service.py` 实现函数体（替换 `raise NotImplementedError`），按 docstring 步骤逐条落。
4. 在 `repository.py` 写查询（必须带 user_id）并在 `models.py` 建 Model，然后启用建表。
5. 把 `routes.py` 里的 `_todo(...)` 换成「校验 + 调 service + `success(...)`」，补 pytest 并用 curl 自测。
6. 单房间物品上限 20，目标格被占推荐最近空位；删除物品不删大脑源文件；同一成就不重复发放奖励。

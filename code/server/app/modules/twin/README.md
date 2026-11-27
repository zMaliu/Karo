# twin — 数字孪生（学伴）

**负责人**：B ｜ **实现 Sprint**：W3-W4 ｜ **当前状态**：接口声明（8 个端点全部返回 501，业务待实现）

## 1. 职责
基于画像的专属 AI 学伴：3 个预设形象、文字流式对话、长期记忆、情绪感知、主动消息、亲密度与历史会话。本期只做文字对话（LLM 先用 mock 打通链路）。

## 2. 端点表（方法 / 路径 / 功能编号 / 负责人 / Sprint / 规格书章节）
| 方法 | 路径 | 功能编号 | 负责人 | Sprint | 规格书 |
|---|---|---|---|---|---|
| POST | `/api/v1/twin/config` | TWN-02 | B | W3 | §3 TWN-02 |
| GET | `/api/v1/twin/profile` | TWN-07 | B | W3 | §3 TWN-07 |
| GET | `/api/v1/twin/messages` | TWN-08 | B | W3 | §3 TWN-08 |
| POST | `/api/v1/twin/messages` | TWN-03 | B | W3 | §3 TWN-03 |
| POST | `/api/v1/twin/memory/search` | TWN-04 | B | 后续 | 后续版本 |
| GET | `/api/v1/twin/proactive` | TWN-06 | B | 后续 | 后续版本 |
| POST | `/api/v1/twin/intimacy` | TWN-07 | B | W3 | §3 TWN-07 |
| GET | `/api/v1/twin/mood` | TWN-05 | B | 后续 | §3 TWN-05 |

所有路径前缀都是 `/api/v1`；完整契约见 `contracts/api.md`，功能逻辑见 `功能实现规格书.md` §3。

## 3. 计划数据表（只写在 models.py 注释里，框架启动不建表）
- twin_profile：id、user_id(唯一 FK)、avatar_id、personality/catchphrases/weakness(JSON)、emotion、intimacy、mood_today、created_at/updated_at
- twin_message：id、user_id(索引)、role(user/assistant)、content、emotion、created_at
- twin_memory：id、user_id(索引)、content、embedding_id、importance、created_at

## 4. 依赖的其他模块
- B(account)：GET /account/profile 画像标签、GET /account/me 昵称与目标。
- C(timer)：GET /timer/stats 今日专注时长（鼓励/催促语）。
- B(brain)：GET /brain/diaries 日记心情，作为对话上下文；未就绪时降级为不带上下文。

## 5. 实现步骤
1. 读 `功能实现规格书.md` §3 中本模块各功能条目（逻辑流程 / 数据变化 / 边界与异常 / 验收）。
2. 在 `schemas.py` 用已声明的 Schema 校验入参（`routes.py` 中 `.load()`），非法 → 422 且不落库。
3. 在 `service.py` 实现函数体（替换 `raise NotImplementedError`），按 docstring 步骤逐条落。
4. 在 `repository.py` 写查询（必须带 user_id）并在 `models.py` 建 Model，然后启用建表。
5. 把 `routes.py` 里的 `_todo(...)` 换成「校验 + 调 service + `success(...)`」，补 pytest 并用 curl 自测。
6. 消息 ≤500 字且空消息不可发；召回为空不编造历史；审核拦截返回安全提示。

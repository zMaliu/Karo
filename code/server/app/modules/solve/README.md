# solve — AI解题室

**负责人**：C ｜ **实现 Sprint**：W3-W4 ｜ **当前状态**：接口声明（10 个端点全部返回 501，业务待实现）

## 1. 职责
拍照/手输题目 → OCR → 分步解题与知识点标签 → 一键收错题本 → 错题筛选与重做。本期先用 mock 解题结果打通链路。

## 2. 端点表（方法 / 路径 / 功能编号 / 负责人 / Sprint / 规格书章节）
| 方法 | 路径 | 功能编号 | 负责人 | Sprint | 规格书 |
|---|---|---|---|---|---|
| POST | `/api/v1/solve/ocr` | SLV-01 | C | W3 | §5 SLV-01 |
| POST | `/api/v1/solve/sessions` | SLV-03 | C | W3 | §5 SLV-03 |
| GET | `/api/v1/solve/sessions/{id}` | SLV-03 | C | W3 | §5 SLV-03 |
| GET | `/api/v1/solve/sessions` | SLV-06 | C | 后续 | 后续版本 |
| POST | `/api/v1/solve/wrongs` | SLV-04 | C | W3 | §5 SLV-04 |
| GET | `/api/v1/solve/wrongs` | SLV-05 | C | W3 | §5 SLV-05 |
| PATCH | `/api/v1/solve/wrongs/{id}` | SLV-05 | C | W3 | §5 SLV-05 |
| DELETE | `/api/v1/solve/wrongs/{id}` | SLV-05 | C | W3 | §5 SLV-05 |
| POST | `/api/v1/solve/hints` | SLV-07 | C | 后续 | 后续版本 |
| POST | `/api/v1/solve/variants` | SLV-08 | C | 后续 | 后续版本 |

所有路径前缀都是 `/api/v1`；完整契约见 `contracts/api.md`，功能逻辑见 `功能实现规格书.md` §5。

## 3. 计划数据表（只写在 models.py 注释里，框架启动不建表）
- solve_session：id、user_id(索引)、subject_tag、source(photo/manual)、question_text、image_url、solution_steps(JSON)、final_answer、knowledge_tags(JSON)、model、status(solved/failed)、created_at/updated_at
- wrong_question：id、user_id(索引)、session_id(FK)、question_text、answer、knowledge_tags(JSON)、wrong_reason、review_status(new/reviewed/mastered)、reviewed_at、created_at/updated_at

## 4. 依赖的其他模块
- 身份：JWT（account 签发）；解题记录与错题仅本人可见（越权 404）。
- B(brain)：GET /brain/notes/{id} 知识点上下文；未就绪时先不拼上下文。
- 被 palace 链接错题（GET /solve/wrongs）；错题知识点供后续学情分析。
- 本期不接真实模型：service.solve 返回 mock 分步过程，TODO 标 R1 流式 + 审核接入点。

## 5. 实现步骤
1. 读 `功能实现规格书.md` §5 中本模块各功能条目（逻辑流程 / 数据变化 / 边界与异常 / 验收）。
2. 在 `schemas.py` 用已声明的 Schema 校验入参（`routes.py` 中 `.load()`），非法 → 422 且不落库。
3. 在 `service.py` 实现函数体（替换 `raise NotImplementedError`），按 docstring 步骤逐条落。
4. 在 `repository.py` 写查询（必须带 user_id）并在 `models.py` 建 Model，然后启用建表。
5. 把 `routes.py` 里的 `_todo(...)` 换成「校验 + 调 service + `success(...)`」，补 pytest 并用 curl 自测。
6. 不确定答案必须标注「需核对」；重复收录同一错题返回 409；图片 ≤10MB、题干预 ≤2000 字。

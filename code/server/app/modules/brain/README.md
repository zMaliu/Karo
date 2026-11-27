# brain — 智脑（学习大脑）

**负责人**：B ｜ **实现 Sprint**：W4 ｜ **当前状态**：接口声明（9 个端点全部返回 501，业务待实现）

## 1. 职责
个人学习资料仓库：文件上传解析、Markdown 笔记、学习日记，并基于本人资料做带引用的问答（RAG）。是学伴上下文、解题知识点、宫殿物品链接的数据底座。

## 2. 端点表（方法 / 路径 / 功能编号 / 负责人 / Sprint / 规格书章节）
| 方法 | 路径 | 功能编号 | 负责人 | Sprint | 规格书 |
|---|---|---|---|---|---|
| POST | `/api/v1/brain/files` | BRN-01 | B | W4 | §4 BRN-01 |
| GET | `/api/v1/brain/files` | BRN-05 | B | W4 | §4 BRN-05 |
| GET | `/api/v1/brain/files/{id}` | BRN-01 | B | W4 | §4 BRN-01 |
| POST | `/api/v1/brain/notes` | BRN-02 | B | W4 | §4 BRN-02 |
| GET | `/api/v1/brain/notes/{id}` | BRN-02 | B | W4 | §4 BRN-02 |
| PATCH | `/api/v1/brain/notes/{id}` | BRN-06 | B | 后续 | 后续版本 |
| POST | `/api/v1/brain/diaries` | BRN-03 | B | W4 | §4 BRN-03 |
| GET | `/api/v1/brain/diaries` | BRN-03 | B | W4 | §4 BRN-03 |
| POST | `/api/v1/brain/chat` | BRN-04 | B | 后续 | 后续版本 |

所有路径前缀都是 `/api/v1`；完整契约见 `contracts/api.md`，功能逻辑见 `功能实现规格书.md` §4。

## 3. 计划数据表（只写在 models.py 注释里，框架启动不建表）
- brain_file：id、user_id(索引)、title、file_type(pdf/image/word/txt)、oss_url、hash(去重)、subject_tag、parse_status(parsing/ok/failed)、summary、created_at/updated_at
- brain_note：id、user_id(索引)、title、content_md、tags(JSON)、created_at/updated_at
- brain_diary：id、user_id(索引)、entry_date、mood、content、created_at/updated_at
- brain_chunk：id、user_id(索引)、source_type(file/note/diary)、source_id、content、embedding_id、created_at

## 4. 依赖的其他模块
- 身份：JWT（account 签发），所有查询必须按 user_id 隔离。
- 被 palace 链接（GET /brain/files/{id}、GET /brain/notes/{id}）、被 solve 取知识点上下文、被 twin 取日记心情。
- 本期不接对象存储/向量库：文件先落本地、检索先用 brain_chunk 关键词匹配，代码里用 TODO 标接入点。

## 5. 实现步骤
1. 读 `功能实现规格书.md` §4 中本模块各功能条目（逻辑流程 / 数据变化 / 边界与异常 / 验收）。
2. 在 `schemas.py` 用已声明的 Schema 校验入参（`routes.py` 中 `.load()`），非法 → 422 且不落库。
3. 在 `service.py` 实现函数体（替换 `raise NotImplementedError`），按 docstring 步骤逐条落。
4. 在 `repository.py` 写查询（必须带 user_id）并在 `models.py` 建 Model，然后启用建表。
5. 把 `routes.py` 里的 `_todo(...)` 换成「校验 + 调 service + `success(...)`」，补 pytest 并用 curl 自测。
6. 删除内容要同步清理切片；问答检索不到时必须明确说「本人资料中未找到」，不臆造。

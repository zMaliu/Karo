# Karo API 索引（/api/v1 · 唯一真源 · 共 53 个端点）

> 框架只声明接口与契约：**53 个端点当前全部返回 501 NOT_IMPLEMENTED**，message 形如
> `twin POST /config：负责人 B / Sprint W3 / 功能 TWN-02 / 规格书 §3 TWN-02`。
> 业务由团队按 `功能实现规格书.md` 逐条实现；LOS 总智能体本期不做（后续单独立项）。

## 通用约定
- 必带请求头 `X-Client-Timezone: Asia/Shanghai`（缺失 400 TIMEZONE_REQUIRED，非法 400 TIMEZONE_INVALID）。
- 成功 `{data, meta}`；失败 `{error:{code,message}, meta}`；鉴权 `Authorization: Bearer <token>`。
- 仅 `account/otp/send`、`account/login` 公开；其余需登录。userId 只从 JWT 取，越权/不存在 404。
- 功能编号 = 模块前缀 + 规格书编号；规格书章节见 `功能实现规格书.md` §1–§6。
- Sprint 标「后续」的是规格书里 ⏳ 的功能，本期不实现（接口仍 501）。

## account 账号与画像（8 · B · W1-W2）
- ★ ACC-01 POST /account/otp/send — 发送验证码（Sprint W1 / 规格书 §1 ACC-01）
- ★ ACC-01 POST /account/login — 登录 / 自动建档（Sprint W1 / 规格书 §1 ACC-01）
- ★ ACC-03 GET /account/me — 我的账号资料（Sprint W1 / 规格书 §1 ACC-03）
- ★ ACC-03 PATCH /account/me — 修改资料（Sprint W1 / 规格书 §1 ACC-03）
- ★ ACC-06 GET /account/profile — 画像标签 + 隐私开关（Sprint W2 / 规格书 §1 ACC-06）
- ★ ACC-06 PUT /account/privacy — 更新隐私偏好（Sprint W2 / 规格书 §1 ACC-06）
- ACC-04 POST /account/questionnaire — 提交 / 重测 25 题问卷（Sprint W2 / 规格书 §1 ACC-04）
- ACC-07 GET /account/devices — 登录设备列表（Sprint W2 / 规格书 §1 ACC-07）

## timer 专注时钟（9 · C · W1-W2）
- ★ TMR-01 POST /timer/sessions — 开始专注（Sprint W1 / 规格书 §2 TMR-01）
- ★ TMR-01 PATCH /timer/sessions/{id} — 暂停 / 继续 / 心跳（Sprint W1 / 规格书 §2 TMR-01）
- ★ TMR-07 POST /timer/sessions/{id}/complete — 完成专注（结算 + 连签，幂等）（Sprint W1 / 规格书 §2 TMR-07）
- ★ TMR-01 POST /timer/sessions/{id}/abort — 放弃本次专注（Sprint W1 / 规格书 §2 TMR-01）
- ★ TMR-08 GET /timer/sessions/active — 进行中会话（重启恢复）（Sprint W1 / 规格书 §2 TMR-08）
- ★ TMR-08 GET /timer/sessions — 专注历史（Sprint W1 / 规格书 §2 TMR-08）
- ★ TMR-08 GET /timer/stats — 今日 / 本周统计（Sprint W1 / 规格书 §2 TMR-08）
- TMR-05 POST /timer/sessions/{id}/interrupt — 中断上报（Sprint W2 / 规格书 §2 TMR-05）
- TMR-08 GET /timer/stats/month — 月度统计（Sprint W2 / 规格书 §2 TMR-08）

## twin 数字孪生（学伴）（8 · B · W3-W4）
- ★ TWN-02 POST /twin/config — 形象选择（Sprint W3 / 规格书 §3 TWN-02）
- ★ TWN-07 GET /twin/profile — 亲密度 / 学伴资料（Sprint W3 / 规格书 §3 TWN-07）
- ★ TWN-08 GET /twin/messages — 历史会话（Sprint W3 / 规格书 §3 TWN-08）
- ★ TWN-03 POST /twin/messages — 流式对话（Sprint W3 / 规格书 §3 TWN-03）
- TWN-04 POST /twin/memory/search — 长期记忆检索（Sprint 后续 / 规格书 后续版本）
- TWN-06 GET /twin/proactive — 主动消息列表（Sprint 后续 / 规格书 后续版本）
- TWN-07 POST /twin/intimacy — 亲密度事件上报（Sprint W3 / 规格书 §3 TWN-07）
- TWN-05 GET /twin/mood — 当前情绪状态（Sprint 后续 / 规格书 §3 TWN-05）

## brain 智脑（学习大脑）（9 · B · W4）
- ★ BRN-01 POST /brain/files — 上传并解析文件（Sprint W4 / 规格书 §4 BRN-01）
- ★ BRN-05 GET /brain/files — 文件列表 / 搜索筛选（Sprint W4 / 规格书 §4 BRN-05）
- ★ BRN-01 GET /brain/files/{id} — 文件详情与切片（Sprint W4 / 规格书 §4 BRN-01）
- ★ BRN-02 POST /brain/notes — 写 Markdown 笔记（Sprint W4 / 规格书 §4 BRN-02）
- ★ BRN-02 GET /brain/notes/{id} — 笔记详情（Sprint W4 / 规格书 §4 BRN-02）
- BRN-06 PATCH /brain/notes/{id} — 编辑笔记 / 自动草稿（Sprint 后续 / 规格书 后续版本）
- BRN-03 POST /brain/diaries — 写学习日记（Sprint W4 / 规格书 §4 BRN-03）
- BRN-03 GET /brain/diaries — 日记时间线（Sprint W4 / 规格书 §4 BRN-03）
- ★ BRN-04 POST /brain/chat — 带引用的资料问答（Sprint 后续 / 规格书 后续版本）

## solve AI解题室（10 · C · W3-W4）
- SLV-01 POST /solve/ocr — 拍照 OCR 识题（Sprint W3 / 规格书 §5 SLV-01）
- ★ SLV-03 POST /solve/sessions — 提交求解（流式）（Sprint W3 / 规格书 §5 SLV-03）
- ★ SLV-03 GET /solve/sessions/{id} — 解题结果（Sprint W3 / 规格书 §5 SLV-03）
- SLV-06 GET /solve/sessions — 解题历史（Sprint 后续 / 规格书 后续版本）
- ★ SLV-04 POST /solve/wrongs — 一键收入错题本（Sprint W3 / 规格书 §5 SLV-04）
- ★ SLV-05 GET /solve/wrongs — 错题筛选 / 重做（Sprint W3 / 规格书 §5 SLV-05）
- SLV-05 PATCH /solve/wrongs/{id} — 补错因 / 标记掌握（Sprint W3 / 规格书 §5 SLV-05）
- SLV-05 DELETE /solve/wrongs/{id} — 删除错题（Sprint W3 / 规格书 §5 SLV-05）
- SLV-07 POST /solve/hints — 引导式分步求解（Sprint 后续 / 规格书 后续版本）
- SLV-08 POST /solve/variants — 变式题推荐（Sprint 后续 / 规格书 后续版本）

## palace 记忆宫殿（9 · C · W4）
- ★ PLS-01 GET /palace/room — 房间初始化 / 读取（Sprint W4 / 规格书 §6 PLS-01）
- ★ PLS-02 POST /palace/items — 摆放物品（Sprint W4 / 规格书 §6 PLS-02）
- ★ PLS-05 PATCH /palace/items/{id} — 移动 / 重命名物品（Sprint W4 / 规格书 §6 PLS-05）
- PLS-05 DELETE /palace/items/{id} — 删除物品（Sprint W4 / 规格书 §6 PLS-05）
- ★ PLS-03 POST /palace/items/{id}/link — 链接文件 / 笔记 / 错题（Sprint W4 / 规格书 §6 PLS-03）
- ★ PLS-04 POST /palace/items/{id}/review — 点击复习并记录（Sprint W4 / 规格书 §6 PLS-04）
- PLS-05 GET /palace/items — 物品管理列表（Sprint W4 / 规格书 §6 PLS-05）
- PLS-06 GET /palace/rewards — 奖励物品列表（Sprint 后续 / 规格书 后续版本）
- PLS-07 PATCH /palace/room — 主题切换（Sprint 后续 / 规格书 后续版本）

## 错误码
400 TIMEZONE_REQUIRED/TIMEZONE_INVALID · 401 UNAUTHORIZED · 404 NOT_FOUND · 409 CONFLICT · 422 VALIDATION_ERROR · 429 TOO_MANY_REQUESTS · 500 INTERNAL_ERROR · 501 NOT_IMPLEMENTED

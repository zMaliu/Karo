# miniprogram — 小程序（5 Tab + 7 页）

页面 / Tab 映射（见 app.json，5 个 Tab 为文字 Tab、不配图标）：
| 页面 | 目录 | 对应模块 | 状态 |
|---|---|---|---|
| 学伴（Tab） | pages/twin | twin | 骨架：静态 UI + PATHS 接口清单 |
| 大脑（Tab） | pages/brain | brain | 骨架：静态 UI + PATHS 接口清单 |
| 解题（Tab） | pages/solve | solve | 骨架：静态 UI + PATHS 接口清单 |
| 宫殿（Tab） | pages/palace | palace | 骨架：静态 UI + PATHS 接口清单 |
| 我的（Tab） | pages/me | account + timer | 已实现：资料/画像/隐私开关 |
| 登录（非 Tab） | pages/login | account | 已实现：手机号+验证码倒计时 |
| 计时（非 Tab） | pages/timer | timer | 已实现：开始/暂停/完成/今日统计/连签 |

A 的每周任务：
- W1：7 页骨架 + 5 Tab + services/request.js + 登录页走通
- W2：我的页（资料/画像/隐私开关）+ 计时页（大数字/统计/连签）
- W3：学伴页（mock 流式气泡）+ 解题页（拍照/结果骨架）
- W4：大脑页（笔记列表）+ 宫殿页（网格骨架）+ 体验版打包

调试：微信开发者工具导入 miniprogram/（无 npm）；登录先调 POST /account/otp/send，dev 模式接口直接回 dev_code；接口路径统一从 services/api.js 的 PATHS 取，不手写 URL。

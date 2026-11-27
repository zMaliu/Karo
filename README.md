# Karo

![CI](https://github.com/zMaliu/Karo/actions/workflows/ci.yml/badge.svg)

备考学生的 AI 学习 OS：微信小程序（原生）+ Flask + MySQL。当前为初版框架，业务按规格书实现。

## 项目结构

```
Karo/
├── docx/                   7 份需求 PDF
├── 功能实现规格书.md         57 个功能的实现规格（开发依据）
├── 开发排期表.xlsx           排期 / 进度 / 分工 / 功能索引
├── 协作规范.md              仓库、分支、提测审查、注意事项
└── code/
    ├── contracts/api.md     53 个端点契约
    ├── server/              Flask 6 模块（全部 501）+ schema.sql（16 张表）
    └── miniprogram/         小程序 7 页（5 Tab）
```

## 启动

### 1. 后端（Flask）

```bash
cd code/server
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python run.py          # http://127.0.0.1:5000
.venv/bin/python -m pytest -q     # 框架测试 9 条
```

默认使用 SQLite（`code/server/karo.db`）；改用 MySQL：`DATABASE_URL="mysql+pymysql://user:pass@127.0.0.1:3306/karo?charset=utf8mb4" .venv/bin/python run.py`（先执行 `schema.sql` 建表）。

### 2. 小程序（微信开发者工具）

1. 打开微信开发者工具 →「导入项目」；
2. 目录选 `code/miniprogram`（AppID 已配测试号 `touristappid`，也可填自己的 AppID）；
3. 详情 → 本地设置 → 勾选「不校验合法域名、web-view（业务域名）、TLS 版本以及 HTTPS 证书」；
4. 确认后端地址：`code/miniprogram/app.js` 中 `baseUrl = 'http://127.0.0.1:5000/api/v1'`（真机预览改成电脑局域网 IP）；
5. 点「编译」，7 个页面可打开；接口当前统一返回 501，页面显示「建设中」。

### 3. 开发文档

- 改哪个文件：`开发排期表.xlsx` →「功能索引」；
- 怎么实现：`功能实现规格书.md` → 对应功能条目；
- 接口契约：`code/contracts/api.md`；表结构：`code/server/schema.sql`；
- 协作流程：`协作规范.md`。

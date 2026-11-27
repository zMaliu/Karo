# Karo

备考学生的 AI 学习 OS（微信小程序 + Flask + MySQL）。当前为初版框架：接口与数据库结构已定义，业务按规格书实现。

## 目录

```
Karo/
├── docx/                 7 份需求 PDF
├── 功能实现规格书.md       全量 57 个功能的实现规格（总指导）
├── 开发排期表.xlsx         排期 / 任务明细 / 功能索引 / 分工（实时进度）
└── code/
    ├── contracts/api.md   53 个端点契约（唯一真源）
    ├── server/            Flask 6 模块（接口声明，全部 501）+ schema.sql（16 张表）
    └── miniprogram/       小程序 7 页（5 Tab）
```

## 怎么定位要写的代码

1. 在 `开发排期表.xlsx` →「功能索引」按功能号查：负责人 / 排期 / 代码模块路径 / 数据表；
2. 打开 `功能实现规格书.md` 对应条目，按流程、数据、边界实现；
3. 按 `code/README.md` 的 5 步落地（schemas → service → repository/model → 替换 501 → 测试）；
4. 完成后回「功能索引」「任务明细」更新状态。

## 启动

```bash
cd code/server
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python run.py        # http://127.0.0.1:5000
.venv/bin/python -m pytest -q   # 框架测试 9 条
```

改接口先改 `code/contracts/api.md`；建表以 `code/server/schema.sql` 为准。
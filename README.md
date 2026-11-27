# Karo

![CI](https://github.com/zMaliu/Karo/actions/workflows/ci.yml/badge.svg)

备考学生的 AI 学习 OS（微信小程序 + Flask + MySQL）。初版框架：接口与数据库结构已定义，业务按规格书实现。

## 文档

| 文件 | 用途 |
|---|---|
| `功能实现规格书.md` | 57 个功能的实现规格（唯一开发依据） |
| `开发排期表.xlsx` | 排期 / 进度 / 分工 / 功能→代码索引 |
| `code/contracts/api.md` | 53 个端点契约（唯一真源） |
| `code/server/schema.sql` | 16 张表结构 |
| `code/README.md` | 框架说明 + 实现一个端点的 5 步 |

## 5 分钟定位要写的代码

1. `开发排期表.xlsx` →「功能索引」按功能号查：负责人 / 分支 / 代码路径 / 数据表；
2. `功能实现规格书.md` 对应条目：接口、流程、数据、边界；
3. `code/README.md` 5 步落地 → 补 pytest → 提 PR。

## 启动

```bash
cd code/server
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python run.py        # http://127.0.0.1:5000
.venv/bin/python -m pytest -q   # 框架测试 9 条
```

## 协作规范

**仓库**：https://github.com/zMaliu/Karo（唯一协作仓库，不要另建或长期 fork）

| 分支 | 谁用 |
|---|---|
| `main` | 所有人只读，受保护，只能经 PR 合并 |
| `frontend` | A 前端 |
| `backend-a` | B（account / twin / brain） |
| `backend-b` | C（timer / solve / palace） |
| `review/*`、`docs/*` | D 审查与文档 |

**每天开工**：

```bash
git switch main && git pull
git switch frontend          # 换成自己的分支
git merge main
```

**提交合并**：`commit -m "feat(功能号): 说明"` → `push 自己分支` → GitHub 开 PR 到 main → CI 绿 + D 审查 → Squash merge。

**注意**：不直接推 main；只改自己分支；PR 一件事且 ≤400 行；改接口先改 `contracts/api.md`；不提交 `.env`/密钥/数据库；冲突在自己分支解决；完成后更新排期表状态。

## 目录

```
Karo/
├── docx/                 7 份需求 PDF
├── 功能实现规格书.md       57 个功能实现规格
├── 开发排期表.xlsx         排期/进度/分工/功能索引
└── code/
    ├── contracts/api.md   53 端点契约
    ├── server/            Flask 6 模块（全 501）+ schema.sql（16 表）
    └── miniprogram/       小程序 7 页（5 Tab）
```
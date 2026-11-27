# Karo

![CI](https://github.com/zMaliu/Karo/actions/workflows/ci.yml/badge.svg)

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

## 协作规范

**协作仓库（唯一）**：https://github.com/zMaliu/Karo 　不要另建仓库或长期 fork。

### 分支

| 分支 | 谁用 | 用途 |
|---|---|---|
| `main` | 所有人只读 | 受保护：只能经 PR 合并，CI 必须绿 |
| `frontend` | A | 小程序页面/请求层 |
| `backend-a` | B | account / twin / brain |
| `backend-b` | C | timer / solve / palace |
| `review/*`、`docs/*` | D | 审查与文档（同样走 PR） |

### 每天开工前（重要）

```bash
git switch main && git pull                 # 1. 先更新 main
git switch frontend                         # 2. 回到自己的分支
git merge main                              # 3. 把 main 合进来（有冲突先解决）
```

### 提交与合并

```bash
git add -A && git commit -m "feat(ACC-01): 手机号登录"   # 4. 小步提交，带功能号
git push origin frontend                                  # 5. 推自己的分支
# 6. 在 GitHub 开 PR → frontend → main，等 CI 绿 + D 审查通过后 Squash merge
```

### 注意事项（10 条）

1. **不要直接 push `main`**（已开分支保护，会被拒绝）。
2. 只在**自己的分支**改代码，别人的分支不动。
3. 写代码前先按上面 3 步同步 `main`，减少冲突。
4. 一个 PR 只做一件事，改动 ≤400 行，描述里写功能号（如 `TMR-07`）。
5. CI 不绿不合并；D 审查通过才算完成。
6. 改接口先改 `code/contracts/api.md`，再改代码，PR 备注契约变更。
7. 不提交密钥/`.env`/数据库文件（`.gitignore` 已覆盖；密钥走环境变量）。
8. 冲突在自己分支解决后重新 push，**禁止 force push `main`**。
9. 每周至少同步一次 `main`；长期不用的分支及时删。
10. 功能完成后更新 `开发排期表.xlsx` 的「状态」列和模块 README。

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
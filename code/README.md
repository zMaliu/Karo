# 接口框架

> 53 个端点全部返回 501；只声明接口与公共层，没有业务实现。业务按 `../功能实现规格书.md` 实现。

## 目录

```
code/
├── contracts/api.md        53 端点契约（方法/路径/功能号/负责人/Sprint）
├── server/
│   ├── schema.sql          数据库结构（16 张表，MySQL 8）
│   ├── app/__init__.py     应用工厂：6 蓝图 + X-Client-Timezone 校验
│   ├── app/common/         信封 / 错误 / JWT / 501 兜底
│   ├── app/modules/<m>/    routes(接口声明) schemas(入参) service(签名) repository(查询) models(表注释) README(分工)
│   └── tests/              框架测试 9 条（路由/501/401/400/信封）
└── miniprogram/            小程序 7 页（PATHS 表来自契约）
```

## 请求链路

```
X-Client-Timezone 校验（400）→ @auth_required JWT（401）→ routes._todo（501，message 含功能号）
实现后：routes(校验) → service(业务) → repository(带 user_id) → models → {data,meta} / {error,meta}
```

## 数据库

初版表结构见 `server/schema.sql`（账号/画像/设备、计时/签到、学伴、智脑、解题/错题、宫殿）。约定：

- 时间存 UTC（DATETIME(3)），自然日按客户端时区换算；
- 查询必须带 `user_id`；跨模块不 JOIN 对方表；
- 改表结构走后续迁移（Alembic），初版可直接执行 schema.sql。

## 实现一个端点（5 步）

1. 读 `功能实现规格书.md` 对应功能条目；
2. 写 `schemas.py` 入参校验（非法 422）；
3. 写 `service.py` 业务（替换 `raise NotImplementedError`）；
4. 写 `repository.py` 查询 + 按 schema.sql 建表；
5. 把 `routes.py` 的 `_todo(...)` 换成「校验 + service + success」，补 1 条 pytest。

## 命令

```bash
cd code/server && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cd code/server && .venv/bin/python -m pytest -q     # 9 条框架测试
cd code/server && .venv/bin/python run.py           # http://127.0.0.1:5000
```
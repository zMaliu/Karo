# 接口框架

> 53 个端点全部返回 501；只有接口声明与公共层，没有业务实现。开发依据：`../功能实现规格书.md`。

## 目录

```
code/
├── contracts/api.md        53 端点契约（方法/路径/功能号/负责人/Sprint）
├── server/
│   ├── schema.sql          16 张表（MySQL 8）
│   ├── app/__init__.py     应用工厂 + X-Client-Timezone 校验
│   ├── app/common/         信封 / 错误 / JWT / 501 兜底
│   ├── app/modules/<m>/    routes(接口) schemas(入参) service(签名) repository(查询) models(表注释)
│   └── tests/              框架测试 9 条（路由/501/401/400/信封）
└── miniprogram/            小程序 7 页
```

## 请求链路

```
时区校验（400）→ JWT 校验（401）→ routes._todo（501，带功能号）
实现后：routes(校验) → service(业务) → repository(带 user_id) → models → {data,meta} / {error,meta}
```

## 数据库

表结构以 `server/schema.sql` 为准；时间存 UTC（DATETIME(3)），自然日按 `X-Client-Timezone` 换算；查询必须带 `user_id`；跨模块不 JOIN 对方表。

## 实现一个端点（5 步）

1. 读规格书对应功能条目；
2. 写 `schemas.py` 入参校验（非法 422）；
3. 写 `service.py` 业务（替换 `raise NotImplementedError`）；
4. 写 `repository.py` 查询 + 按 schema.sql 建表；
5. 把 `routes.py` 的 `_todo(...)` 换成「校验 + service + success」，补 1 条 pytest。

## 命令

```bash
cd code/server && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cd code/server && .venv/bin/python -m pytest -q
cd code/server && .venv/bin/python run.py
```
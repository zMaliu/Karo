from flask_sqlalchemy import SQLAlchemy

# 框架阶段不建表；团队在 models.py 写 Model 后使用本实例，并启用 app/__init__.py 的建表代码
db = SQLAlchemy()

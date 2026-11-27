from zoneinfo import ZoneInfo

from flask import Flask, g, request

from app.common.errors import ApiError, register_error_handlers
from app.config import Config
from app.extensions import db


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)

    # 6 个业务模块显式注册（无自动发现）：routes 只声明接口，业务由团队按规格书实现
    from app.modules.account.routes import bp as account_bp
    from app.modules.brain.routes import bp as brain_bp
    from app.modules.palace.routes import bp as palace_bp
    from app.modules.solve.routes import bp as solve_bp
    from app.modules.timer.routes import bp as timer_bp
    from app.modules.twin.routes import bp as twin_bp

    for module_bp in (account_bp, timer_bp, twin_bp, brain_bp, solve_bp, palace_bp):
        app.register_blueprint(module_bp)
    register_error_handlers(app)

    @app.before_request
    def require_client_timezone():
        # 自然日/统计口径都依赖客户端时区：每个请求必须带 IANA 时区，否则 400
        tz_name = request.headers.get("X-Client-Timezone", "").strip()
        if not tz_name:
            raise ApiError("TIMEZONE_REQUIRED", "缺少 X-Client-Timezone 请求头", 400)
        try:
            g.client_tz = ZoneInfo(tz_name)
        except Exception:
            raise ApiError("TIMEZONE_INVALID", "X-Client-Timezone 不是合法 IANA 时区", 400) from None
        g.client_tz_name = tz_name

    # 建表由团队完成：models.py 写好 Model 后再启用下面两行（框架阶段不建任何表）
    # with app.app_context():
    #     db.create_all()
    return app

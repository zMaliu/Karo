from flask import current_app
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from app.common.response import failure


class ApiError(Exception):
    """业务错误：service 层抛出，统一转成 {error, meta} 信封。"""

    def __init__(self, code, message, status=400):
        super().__init__(message)
        self.code = code
        self.message = message
        self.status = status


def register_error_handlers(app):
    @app.errorhandler(ApiError)
    def handle_api_error(err):
        return failure(err.code, err.message, err.status)

    @app.errorhandler(NotImplementedError)
    def handle_not_implemented(err):
        # service/repository 函数体默认 raise NotImplementedError，框架统一兜底为 501 占位
        return failure("NOT_IMPLEMENTED", str(err) or "接口待实现", 501)

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        if isinstance(err.messages, dict):
            message = "; ".join(f"{field}: {'/'.join(msgs)}" for field, msgs in err.messages.items())
        else:
            message = str(err.messages)
        return failure("VALIDATION_ERROR", message or "参数不合法", 422)

    @app.errorhandler(HTTPException)
    def handle_http_error(err):
        return failure(err.name.upper().replace(" ", "_"), err.description, err.code)

    @app.errorhandler(Exception)
    def handle_unexpected_error(err):
        current_app.logger.exception("unhandled error")
        return failure("INTERNAL_ERROR", "服务异常", 500)

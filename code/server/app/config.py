import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    """框架配置：只保留鉴权与后续建表需要的最小项。"""

    SECRET_KEY = os.getenv("SECRET_KEY", "karo-dev-secret")
    JWT_TTL_SECONDS = int(os.getenv("JWT_TTL_SECONDS", str(7 * 24 * 3600)))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "karo.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

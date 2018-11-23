"""Docsstring for config.py."""
import os


class Config(object):
    """docstring for Config."""

    DEBUG = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY = "fiona"


class DevelopmentConfig(Config):
    """docstring for DevelopmentConfig."""

    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv('DATABASE_DEVELOP')


class TestingConfig(Config):
    """docstring for TestingConfig."""

    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv('DATABASE_TEST')


class StagingConfig(Config):
    """docstring for StagingConfig."""

    DEBUG = True


class ProductionConfig(Config):
    """docstring for ProductionConfig."""

    DEBUG = False
    TESTING = False
    DATABASE_URL = 'postgres://lzkeoyabateebv:2eeda542ecd71f311f82018d4528f7e7c4f6118444b5847b80097e79333c67b9@ec2-54-204-36-249.compute-1.amazonaws.com:5432/d7be81aif8bjb0'


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
    "production": ProductionConfig
}

"""Docsstring for config.py."""
import os


class Config(object):
    """docstring for Config."""

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """docstring for DevelopmentConfig."""

    DEBUG = True
    TESTING = False
    DATABASE_URL = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    """docstring for TestingConfig."""

    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv('DATABASE_TESTING_URL')


class StagingConfig(Config):
    """docstring for StagingConfig."""

    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """docstring for ProductionConfig."""

    pass


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig
}

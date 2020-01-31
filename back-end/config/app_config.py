import os


class Config:
    DEBUG = False
    THREADED = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'jl=r!r#fjqn+g!o^ktlw7yxta6$xh5koctmi-9#ma1%_78!-r4')
    APP_PORT = int(os.getenv('APP_PORT', 8002))

    APP_ENV = os.getenv('APP_ENV', 'DEV')
    API_URL_PREFIX = '/api'

    DB_USERNAME = 'pusher_user'
    DB_PASSWORD = 'pusher_pass'
    DB_NAME = 'pusher_db'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    'DEV': DevelopmentConfig,
    'PROD': ProductionConfig
}

from decouple import config

class AppConfig:
    class FlaskConfig:
        APP = config('FLASK_APP', default='app.py')
        ENV = config('FLASK_ENV', default='development')
        DEBUG = config('FLASK_DEBUG', default=True, cast=bool)
        RUN_HOST = config('FLASK_RUN_HOST', default='0.0.0.0')
        RUN_PORT = config('FLASK_RUN_PORT', default=4001, cast=int)
    class PgDbConfig:
    # Database settings
        SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI', default='postgresql://postgres:postgres@localhost/postgres')
        SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)
    class AppSettingsConfig:
    # Application settings
        SECRET_KEY = config('SECRET_KEY', default='your-secret-key')
        APP_PASSWORD = config('APP_PASSWORD', default='admin')
class DevelopmentConfig(AppConfig):
    FLASK_ENV = 'development'
    FLASK_DEBUG = True

class ProductionConfig(AppConfig):
    FLASK_ENV = 'production'
    FLASK_DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
env = AppConfig.FlaskConfig.ENV
key = AppConfig.AppSettingsConfig.SECRET_KEY
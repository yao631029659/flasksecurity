class Config(object):
    DEBUG = True
    SECRET_KEY = '6LfOUhAUAAAAAHiszVGQsv9VO2NCBRsHbEwsvOxr'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # 允许自定义视图模板
    SECURITY_REGISTERABLE = True
class Config(object):
    DEBUG = True
    SECRET_KEY = '6LfOUhAUAAAAAHiszVGQsv9VO2NCBRsHbEwsvOxr'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # 允许自定义视图模板
    SECURITY_REGISTERABLE = True
    SECURITY_EMAIL_SENDER = 'm15913955859@163.com'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'm15913955859'
    # 这个授权码不是密码 在邮箱设置里面有 请不要乱用
    MAIL_PASSWORD = 's87654321'
    # 注册的时候不发送邮件
    # SECURITY_SEND_REGISTER_EMAIL=False
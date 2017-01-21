from flask_security import SQLAlchemyUserDatastore
from webapp.models import db,User,Role
from flask_mail import Mail
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
mail = Mail()
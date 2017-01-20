from flask_security import SQLAlchemyUserDatastore
from webapp.models import db,User,Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
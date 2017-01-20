from flask import Flask, render_template
from flask_security import Security,login_required
from flask_security.utils import logout_user
from webapp.models import db,user_datastore

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

db.init_app(app)




# 实例化Security需要两个参数
security = Security(app, user_datastore)

# Create a user to test with
# 在request之前执行数据库添加操作
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='matt@nobien.net', password='password')
    db.session.commit()

# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')
@app.route('/logout')
def logout():
    logout_user()


if __name__ == '__main__':
    app.run()
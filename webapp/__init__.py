from flask import Flask, render_template
from flask_security import Security,login_required,roles_required
from flask_security.utils import logout_user
from webapp.extension import user_datastore,mail
from webapp.models import db,User
from webapp.config import Config

# Create app
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
mail.init_app(app)



# 实例化Security需要两个参数
security = Security(app, user_datastore)

# Create a user to test with
# 在request之前执行数据库添加操作
# @app.before_first_request
# def create_user():
#     db.create_all()
#     user1=user_datastore.create_user(email='yoyo3', password='12345678')
#     role1=user_datastore.create_role(name='admin',description='系统管理员')
#     user_datastore.add_role_to_user(user1,role1)
#     db.session.commit()

# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')
@app.route('/logout')
def logout():
    logout_user()

@app.route('/secret')
# 只允许特定角色使用
@login_required
# @roles_required('admin', 'editor') admin和edit是and的关系
# @roles_required('admin')
def secret():
    return render_template(
        'secret.html',
    )


if __name__ == '__main__':
    app.run()
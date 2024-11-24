from flask import Flask
from config import Config
from blueprints.blueprint1 import home_bp
from blueprints.blueprint2 import user_bp
from models import db

app = Flask(__name__)
app.config.from_object(Config)

# 初始化数据库
db.init_app(app)

# 注册蓝图
app.register_blueprint(home_bp)
app.register_blueprint(user_bp)

# 创建数据库所有表
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

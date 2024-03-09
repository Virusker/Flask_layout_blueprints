from flask import Flask

app = Flask(__name__,static_folder='../static',template_folder='../templates')
app.config.from_pyfile('../config.py')

# đăng kí blueprint
from views.index import index_bp
app.register_blueprint(index_bp)

from views.admin import admin_bp
app.register_blueprint(admin_bp)
from flask import Blueprint, render_template

# sử dụng thêm các tùy chọn để config static_folder và template_folder tùy chỉnh
# index = Blueprint('index', __name__, static_folder='static', template_folder='templates')
index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')
from flask import Blueprint, render_template

# sử dụng thêm các tùy chọn để config static_folder và template_folder tùy chỉnh
# admin_bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates')
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin():
    return render_template('admin.html')

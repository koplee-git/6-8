from flask import Blueprint, request, current_app
from flask import render_template
from simpledu.decorators import admin_required
from simpleu.models import Course
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def admin_index():
    return 'admin'
@admin.route('/courses')
@admin_required
def index():
    page = request.args.get('page',default=1,type=int)
    pagination = Course.query.paginate(
    per_page=current_app.config['ADMIN_PRE_PAGE'],
    error_out=False
    )
    return render_template('admin/index.html',pagination=pagination)

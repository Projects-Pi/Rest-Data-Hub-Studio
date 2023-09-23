from flask import Blueprint

# tasks_bp = Blueprint('tasks', __name__)
# admin_routes = Blueprint('admin_routes', __name__)
# user_routes = Blueprint('user_routes', __name__)

from . import tasks
from . import admin_routes
from . import user_routes

def register_blueprints(app):
    app.register_blueprint(tasks.tasks_bp, url_prefix='/tasks')
    app.register_blueprint(admin_routes.admin_routes, url_prefix='/admin')
    app.register_blueprint(user_routes.user_routes, url_prefix='/user')

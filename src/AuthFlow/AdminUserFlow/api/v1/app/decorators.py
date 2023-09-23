from functools import wraps
from flask import request, jsonify, make_response
from models import Entity  # Import your Entity model
import traceback
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            admin_id = request.get_json().get('admin_id')
            admin_password = request.get_json().get('admin_password')

            # Check if the requester is an admin (you can implement your own admin authentication logic)
            requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

            if not requester_admin:
                return make_response(jsonify({'message': 'Admin not found'}), 404)

            if not requester_admin.check_password(admin_password):
                return make_response(jsonify({'message': 'Invalid admin password'}), 401)

            return f(*args, **kwargs)

        except Exception as e:
            traceback.print_exc()
            return make_response(jsonify({'message': 'Error authorizing admin'}), 500)
    return decorated_function

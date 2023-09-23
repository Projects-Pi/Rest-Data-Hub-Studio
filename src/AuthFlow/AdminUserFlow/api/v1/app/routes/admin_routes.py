from flask import Blueprint, request, jsonify, make_response
from models import db, Entity, Role, EntityRole
from decorators import admin_required
import traceback

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
# Create a blueprint for admin-related routes
admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/register', methods=['POST'])
#@admin_required  # This decorator checks if the user is an admin
def register_admin():
    try:
        data = request.get_json()
        app_password = data.get('app_password')

        # Check if the provided app password is correct
        if app_password != 'KQQbfA93uPdjgsUv':
            return make_response(jsonify({'message': 'Invalid application password'}), 401)

        # Create a new admin (entity_type set to 'admin')
        new_admin = Entity(username=data['username'], email=data['email'], password=data['password'], entity_type='admin')
        db.session.add(new_admin)
        db.session.commit()

        return make_response(jsonify({'message': 'Admin registered successfully'}), 201)
    except Exception as e:
        traceback.print_exc()
        return make_response(jsonify({'message': 'Error registering admin'}), 500)

@admin_routes.route('/assign_role', methods=['POST'])
@admin_required
def assign_role():
    try:
        data = request.get_json()
        admin_id = data.get('admin_id')
        entity_id = data.get('entity_id')
        role_name = data.get('role_name')

        # Check if the requester is an admin (you can implement your own admin authentication logic)
        requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

        if not requester_admin:
            return make_response(jsonify({'message': 'Admin not found'}), 404)

        if not requester_admin.check_password(data.get('admin_password')):
            return make_response(jsonify({'message': 'Invalid admin password'}), 401)

        role = Role.query.filter_by(name=role_name).first()
        entities = Entity.query.filter_by(id=entity_id).first()
        if not entities:
            return make_response(jsonify({'message': 'entity_id not found'}), 404)
        if not role:
            return make_response(jsonify({'message': 'Role not found'}), 404)

        if entity_id:
            entity_role = EntityRole(entity_id=entity_id, role_id=role.id, entity_type=entities.entity_type)
            db.session.add(entity_role)
        else:
            return make_response(jsonify({'message': 'Invalid entity ID'}), 400)

        db.session.commit()
        return make_response(jsonify({'message': 'Role assigned successfully'}), 200)
    except Exception as e:
        traceback.print_exc()
        return make_response(jsonify({'message': 'Error assigning role'}), 500)

@admin_routes.route('/update/<int:id>', methods=['PUT'])
@admin_required
def update_admin(id):
    try:
        admin = Entity.query.filter_by(id=id, entity_type='admin').first()
        if admin:
            data = request.get_json()
            admin.username = data.get('username', admin.username)
            admin.email = data.get('email', admin.email)
            
            # Hash the new password if it's provided in the request
            new_password = data.get('password')
            if new_password:
                admin.password = bcrypt.generate_password_hash(new_password).decode('utf-8')

            db.session.commit()
            return make_response(jsonify({'message': 'Admin updated'}), 200)
        return make_response(jsonify({'message': 'Admin not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error updating admin'}), 500)

@admin_routes.route('/delete/<int:id>', methods=['DELETE'])
@admin_required
def delete_admin(id):
    try:
        admin = Entity.query.filter_by(id=id, entity_type='admin').first()
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return make_response(jsonify({'message': 'Admin deleted'}), 200)
        return make_response(jsonify({'message': 'Admin not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error deleting admin'}), 500)
@admin_routes.route('/list_admins', methods=['GET'])
@admin_required
def list_admins():
    try:
        data = request.get_json()
        admin_id = data.get('admin_id')
        admin_password = data.get('admin_password')

        # Check if the requester is an admin (you can implement your own admin authentication logic)
        requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

        if not requester_admin:
            return make_response(jsonify({'message': 'Admin not found'}), 404)

        if not requester_admin.check_password(admin_password):
            return make_response(jsonify({'message': 'Invalid admin password'}), 401)

        admins = Entity.query.filter_by(entity_type='admin').all()
        return make_response(jsonify([admin.json() for admin in admins]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Error getting admins'}), 500)

@admin_routes.route('/list_users', methods=['GET'])
@admin_required
def list_users():
    try:
        data = request.get_json()
        admin_id = data.get('admin_id')
        admin_password = data.get('admin_password')

        # Check if the requester is an admin (you can implement your own admin authentication logic)
        requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

        if not requester_admin:
            return make_response(jsonify({'message': 'Admin not found'}), 404)

        if not requester_admin.check_password(admin_password):
            return make_response(jsonify({'message': 'Invalid admin password'}), 401)

        users = Entity.query.filter_by(entity_type='user').all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Error getting users'}), 500)

@admin_routes.route('/approve_user/<int:user_id>', methods=['POST'])
@admin_required
def approve_user(user_id):
    try:
        admin_id = request.get_json().get('admin_id')
        admin_password = request.get_json().get('admin_password')

        # Check if the requester is an admin (you can implement your own admin authentication logic)
        requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

        if not requester_admin:
            return make_response(jsonify({'message': 'Admin not found'}), 404)

        if not requester_admin.check_password(admin_password):
            return make_response(jsonify({'message': 'Invalid admin password'}), 401)

        user = Entity.query.filter_by(id=user_id, entity_type='user').first()
        if user:
            user.entity_status = 'active'
            db.session.commit()
            return make_response(jsonify({'message': 'User approved'}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error approving user'}), 500)

@admin_routes.route('/revoke_user/<int:user_id>', methods=['POST'])
@admin_required
def revoke_user(user_id):
    try:
        admin_id = request.get_json().get('admin_id')
        admin_password = request.get_json().get('admin_password')

        # Check if the requester is an admin (you can implement your own admin authentication logic)
        requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

        if not requester_admin:
            return make_response(jsonify({'message': 'Admin not found'}), 404)

        if not requester_admin.check_password(admin_password):
            return make_response(jsonify({'message': 'Invalid admin password'}), 401)

        user = Entity.query.filter_by(id=user_id, entity_type='user').first()
        if user:
            user.entity_status = 'revoked'
            db.session.commit()
            return make_response(jsonify({'message': 'User revoked'}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error revoking user'}), 500)

# @admin_routes.route('/list', methods=['GET'])
# @admin_required
# def list_admins():
#     try:
#         data = request.get_json()
#         admin_id = data.get('admin_id')
#         admin_password = data.get('admin_password')

#         # Check if the requester is an admin (you can implement your own admin authentication logic)
#         requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

#         if not requester_admin:
#             return make_response(jsonify({'message': 'Admin not found'}), 404)

#         if not requester_admin.check_password(admin_password):
#             return make_response(jsonify({'message': 'Invalid admin password'}), 401)

#         admins = Entity.query.filter_by(entity_type='admin').all()
#         return make_response(jsonify([admin.json() for admin in admins]), 200)
#     except Exception as e:
#         return make_response(jsonify({'message': 'Error getting admins'}), 500)


# @admin_routes.route('/approve_user/<int:user_id>', methods=['POST'])
# @admin_required
# def approve_user(user_id):
#     try:
#         user = Entity.query.filter_by(id=user_id, entity_type='user').first()
#         if user:
#             user.user_status = 'active'
#             db.session.commit()
#             return make_response(jsonify({'message': 'User approved'}), 200)
#         return make_response(jsonify({'message': 'User not found'}), 404)
#     except Exception as e:
#         return make_response(jsonify({'message': 'Error approving user'}), 500)

# @admin_routes.route('/revoke_user/<int:user_id>', methods=['POST'])
# @admin_required
# def revoke_user(user_id):
#     try:
#         user = Entity.query.filter_by(id=user_id, entity_type='user').first()
#         if user:
#             user.user_status = 'revoked'
#             db.session.commit()
#             return make_response(jsonify({'message': 'User revoked'}), 200)
#         return make_response(jsonify({'message': 'User not found'}), 404)
#     except Exception as e:
#         return make_response(jsonify({'message': 'Error revoking user'}), 500)

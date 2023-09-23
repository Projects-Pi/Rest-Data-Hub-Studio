from flask import Blueprint, request, jsonify, make_response
from models import db, Entity, Role, EntityRole
from decorators import admin_required  # Import your admin authentication decorator

# Create a blueprint for user-related routes
user_routes = Blueprint('user_routes', __name__)

# User registration route
@user_routes.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return make_response(jsonify({'message': 'Missing username, email, or password'}), 400)

        # Check if a user with the same email already exists
        existing_user = Entity.query.filter_by(email=email).first()
        if existing_user:
            return make_response(jsonify({'message': 'Email address already in use'}), 409)

        # Create a new user (entity_type set to 'user')
        new_user = Entity(username=username, email=email, password=password, entity_type='user')
        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify({'message': 'User registered successfully'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'Error registering user'}), 500)

# User login route
@user_routes.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return make_response(jsonify({'message': 'Missing email or password'}), 400)

        # Find the user by email
        user = Entity.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            return make_response(jsonify({'message': 'Invalid email or password'}), 401)

        # Check if the user is approved (user_status is 'approved')
        if user.user_status != 'active':
            return make_response(jsonify({'message': 'User not approved'}), 403)

        return make_response(jsonify({'message': 'User logged in successfully'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Error logging in'}), 500)
# Get all users
@user_routes.route('/', methods=['GET'])
@admin_required  # Require admin access to get all users
def get_users():
    try:
        admin_id = request.get_json().get('admin_id')
        admin_password = request.get_json().get('admin_password')

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

# Get a user by ID
@user_routes.route('/<int:id>', methods=['GET'])
@admin_required  # Require admin access to get a user by ID
def get_user(id):
    try:
        admin_id = request.get_json().get('admin_id')
        admin_password = request.get_json().get('admin_password')

        # Check if the requester is an admin (you can implement your own admin authentication logic)
        requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

        if not requester_admin:
            return make_response(jsonify({'message': 'Admin not found'}), 404)

        if not requester_admin.check_password(admin_password):
            return make_response(jsonify({'message': 'Invalid admin password'}), 401)

        user = Entity.query.filter_by(id=id, entity_type='user').first()
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error getting user'}), 500)

# Update a user
@user_routes.route('/<int:id>', methods=['PUT'])
@admin_required  # Require admin access to update a user
def update_user(id):
    try:
        admin_id = request.get_json().get('admin_id')
        admin_password = request.get_json().get('admin_password')

        # Check if the requester is an admin (you can implement your own admin authentication logic)
        requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

        if not requester_admin:
            return make_response(jsonify({'message': 'Admin not found'}), 404)

        if not requester_admin.check_password(admin_password):
            return make_response(jsonify({'message': 'Invalid admin password'}), 401)

        user = Entity.query.filter_by(id=id, entity_type='user').first()
        if user:
            data = request.get_json()
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.password = data.get('password', user.password)  # You may want to hash the new password here
            db.session.commit()
            return make_response(jsonify({'message': 'User updated'}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error updating user'}), 500)

# Delete a user
@user_routes.route('/<int:id>', methods=['DELETE'])
@admin_required  # Require admin access to delete a user
def delete_user(id):
    try:
        admin_id = request.get_json().get('admin_id')
        admin_password = request.get_json().get('admin_password')

        # Check if the requester is an admin (you can implement your own admin authentication logic)
        requester_admin = Entity.query.filter_by(id=admin_id, entity_type='admin').first()

        if not requester_admin:
            return make_response(jsonify({'message': 'Admin not found'}), 404)

        if not requester_admin.check_password(admin_password):
            return make_response(jsonify({'message': 'Invalid admin password'}), 401)

        user = Entity.query.filter_by(id=id, entity_type='user').first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'User deleted'}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'Error deleting user'}), 500)

# # Get all users
# @user_routes.route('/', methods=['GET'])
# @admin_required  # Require admin access to get all users
# def get_users():
#     try:
#         users = Entity.query.filter_by(entity_type='user').all()
#         return make_response(jsonify([user.json() for user in users]), 200)
#     except Exception as e:
#         return make_response(jsonify({'message': 'Error getting users'}), 500)

# # Get a user by ID
# @user_routes.route('/<int:id>', methods=['GET'])
# @admin_required  # Require admin access to get a user by ID
# def get_user(id):
#     try:
#         user = Entity.query.filter_by(id=id, entity_type='user').first()
#         if user:
#             return make_response(jsonify({'user': user.json()}), 200)
#         return make_response(jsonify({'message': 'User not found'}), 404)
#     except Exception as e:
#         return make_response(jsonify({'message': 'Error getting user'}), 500)

# # Update a user
# @user_routes.route('/<int:id>', methods=['PUT'])
# @admin_required  # Require admin access to update a user
# def update_user(id):
#     try:
#         user = Entity.query.filter_by(id=id, entity_type='user').first()
#         if user:
#             data = request.get_json()
#             user.username = data.get('username', user.username)
#             user.email = data.get('email', user.email)
#             user.password = data.get('password', user.password)  # You may want to hash the new password here
#             db.session.commit()
#             return make_response(jsonify({'message': 'User updated'}), 200)
#         return make_response(jsonify({'message': 'User not found'}), 404)
#     except Exception as e:
#         return make_response(jsonify({'message': 'Error updating user'}), 500)

# # Delete a user
# @user_routes.route('/<int:id>', methods=['DELETE'])
# @admin_required  # Require admin access to delete a user
# def delete_user(id):
#     try:
#         user = Entity.query.filter_by(id=id, entity_type='user').first()
#         if user:
#             db.session.delete(user)
#             db.session.commit()
#             return make_response(jsonify({'message': 'User deleted'}), 200)
#         return make_response(jsonify({'message': 'User not found'}), 404)
#     except Exception as e:
#         return make_response(jsonify({'message': 'Error deleting user'}), 500)

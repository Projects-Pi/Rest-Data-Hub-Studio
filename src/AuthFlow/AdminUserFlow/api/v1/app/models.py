from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, date
from sqlalchemy.orm import validates

bcrypt = Bcrypt()
db = SQLAlchemy()

class AuthInfo(db.Model):
    __tablename__ = 'auth_info'

    id = db.Column(db.Integer, primary_key=True)
    auth_token = db.Column(db.String(255), nullable=False, unique=True)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    end_timestamp = db.Column(db.DateTime, nullable=False)
    entity_name = db.Column(db.String(50), nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)
    role_id = db.Column(db.Integer, nullable=False)
    expiry_period = db.Column(db.Integer, default=1, nullable=False)

    def __init__(self, auth_token, created_timestamp, end_timestamp, entity_name, entity_id, role_id, expiry_period=1):
        self.auth_token = auth_token
        self.created_timestamp = created_timestamp
        self.end_timestamp = end_timestamp
        self.entity_name = entity_name
        self.entity_id = entity_id
        self.role_id = role_id
        self.expiry_period = expiry_period

    @classmethod
    def update_expiry_period(cls, session, auth_info_id, new_expiry_period):
        # Check if the user is an admin before allowing the update
        auth_info = cls.query.filter_by(id=auth_info_id).first()
        if auth_info.entity_role.name == 'admin':
            auth_info.expiry_period = new_expiry_period
            db.session.commit()
        else:
            raise PermissionError("Only admins can update the expiry period")
    @validates('entity_id')
    def validate_entity_role(self, key, value):
        if not EntityRole.query.filter_by(entity_id=value).first():
            raise ValueError("Entity does not exist in entity_roles")
        return value
    @validates('role_id')
    def validate_entity_role(self, key, value):
        if not Role.query.filter_by(id=value).first():
            raise ValueError("Role does not exist in entity_roles")
        return value

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    completed = db.Column(db.Boolean)

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    can_create = db.Column(db.Boolean, default=False, nullable=False)
    can_read = db.Column(db.Boolean, default=False, nullable=False)
    can_update = db.Column(db.Boolean, default=False, nullable=False)
    can_delete = db.Column(db.Boolean, default=False, nullable=False)

class Entity(db.Model):
    __tablename__ = 'entities'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    entity_type = db.Column(db.String(20), nullable=False)
    entity_status = db.Column(db.String(20), nullable=False)
    entity = db.relationship('Entity', secondary='entity_roles')
    def __init__(self, username, email, password, entity_type):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.entity_type = entity_type
        self.set_default_entity_status()

    def set_default_entity_status(self):
        if self.entity_type == 'admin':
            self.entity_status = 'active'
        elif self.entity_type == 'user':
            self.entity_status = 'inactive'

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'entity_type': self.entity_type, 'entity_status': self.entity_status}

class EntityRole(db.Model):
    __tablename__ = 'entity_roles'

    entity_id = db.Column(db.Integer, db.ForeignKey('entities.id'), primary_key=True, nullable=False, unique=True)
    role_id = db.Column(db.Integer, nullable=False)
    entity_type = db.Column(db.String(20), nullable=False)





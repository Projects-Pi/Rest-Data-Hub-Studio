from flask import Flask, request, jsonify, make_response
from models import db, Entity, Role, EntityRole, AuthInfo
from routes import register_blueprints
import app_config
from app_config import AppConfig
from app_config import ProductionConfig
from app_config import DevelopmentConfig

app = Flask(__name__)


# Access the environment configuration from app_config
env = app_config.env

# Load the appropriate configuration based on the environment
if env == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Apply additional configurations from AppConfig
app.config.update(AppConfig.FlaskConfig.__dict__)
app.config.update(AppConfig.PgDbConfig.__dict__)
app.config.update(AppConfig.AppSettingsConfig.__dict__)

db.init_app(app)
register_blueprints(app)
@app.cli.command()
def list_routes():
    """
    Custom CLI command to list all routes and their endpoints.
    """
    print("Available Routes:")
    for rule in app.url_map.iter_rules():
        print(f"Route: {rule.rule}, Endpoint: {rule.endpoint}")


# Routes for AuthInfo
@app.route('/create_auth_info', methods=['POST'])
def create_auth_info():
    data = request.get_json()
    auth_token = data.get('auth_token')
    end_timestamp = data.get('end_timestamp')
    entity_name = data.get('entity_name')
    entity_id = data.get('entity_id')
    role_id = data.get('role_id')
    created_timestamp=data.get('created_timestamp')
    
    auth_info = AuthInfo(auth_token=auth_token, end_timestamp=end_timestamp, entity_name=entity_name,
                         entity_id=entity_id, role_id=role_id,created_timestamp=created_timestamp)
    
    db.session.add(auth_info)
    db.session.commit()
    
    return jsonify(message='AuthInfo created successfully'), 201

@app.route('/update_expiry_period/<int:auth_info_id>', methods=['PUT'])
def update_expiry_period(auth_info_id):
    new_expiry_period = request.get_json().get('new_expiry_period')
    
    auth_info = AuthInfo.query.get(auth_info_id)
    if not auth_info:
        return jsonify(message='AuthInfo not found'), 404
    
    # Check if the user is an admin before allowing the update
    if auth_info.role.name == 'admin':
        auth_info.expiry_period = new_expiry_period
        db.session.commit()
        return jsonify(message='Expiry period updated successfully'), 200
    else:
        return jsonify(message='Only admins can update the expiry period'), 403

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    host = app.config['RUN_HOST']
    port = app.config['RUN_PORT']
    debug = app.config['DEBUG']
    
    print(f"Running in {env} environment")
    
    app.run(
        host=host,
        port=port,
        debug=debug,
    )
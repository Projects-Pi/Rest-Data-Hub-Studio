# from flask import Flask
# from models import db
# from routes import register_blueprints
# from config import Config

# def create_app(config):
#     app = Flask(__name__)
    
#     # Load configuration from the provided Config class
#     app.config.from_object(config)

#     pg_db_config = config.PgDbConfig
#     database_url = pg_db_config.SQLALCHEMY_DATABASE_URI

#     # Configure the Flask app with the database URL
#     app.config['SQLALCHEMY_DATABASE_URI'] = database_url

#     #db.init_app(app)

#     # Register the blueprint(s)
#     #register_blueprints(app)
    
#     return app # Return both the app and its configuration

# #app, flask_config = create_app(Config)

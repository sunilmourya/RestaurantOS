from flask import Flask
from .utils.database import init_app


def create_app():
    app = Flask(__name__)

    # Configure your database URI here
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database and migrations
    init_app(app)

    # Register blueprints, e.g., auth, user
    from .routes.auth_routes import bp as auth_bp
    app.register_blueprint(auth_bp)

    # from .routes.user_routes import bp as user_bp
    # app.register_blueprint(user_bp)

    # Other configurations and blueprints...

    return app

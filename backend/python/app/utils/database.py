from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create SQLAlchemy and Migrate instances
db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    """
    Initialize the database and migration instances with the Flask application.
    """
    db.init_app(app)
    migrate.init_app(app, db)

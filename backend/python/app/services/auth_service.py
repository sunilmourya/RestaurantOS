from ..models.user import User
from ..utils.database import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

SECRET_KEY = 'your_secret_key'

def register_user(data):
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password, role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

def login_user(data):
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode({'username': user.username}, SECRET_KEY, algorithm='HS256')
        return token
    return None

def logout_user(token):
    # Implement token invalidation if necessary
    pass

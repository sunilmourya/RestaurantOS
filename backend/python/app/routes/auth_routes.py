from flask import Blueprint, jsonify, request
from ..services.auth_service import register_user, login_user, logout_user

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = register_user(data)
    return jsonify(user), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = login_user(data)
    return jsonify({'token': token}), 200

@bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    logout_user(token)
    return jsonify({'message': 'Logged out'}), 200

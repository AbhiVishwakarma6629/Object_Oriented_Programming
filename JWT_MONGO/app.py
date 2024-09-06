from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your_secret_key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['user_db']
users_collection = db['users']
blacklist_collection = db['blacklisted_tokens']


@app.route('/register', methods = ['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg" : 'Username and Password are required......!'}),400
    
    existing_user = users_collection.find_one({'username' : username})
    if existing_user:
        return jsonify({'msg' : 'User already exists'}),409

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({'username' : username, 'password' : hashed_password})

    access_token = create_access_token(identity=username)
    return jsonify({'msg' : 'User registered successfully!', 'access token' : access_token})


@app.route('/login', methods=['POST'])
@jwt_required()
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users_collection.find_one({'username' : username})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'msg' : 'Invalid username or password!'}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify({'msg' : f" Welcome {username} "}), 200


@app.route('/logout', methods = ['POST'])
@jwt_required()
def logout():
    jti = get_jwt_identity()
    blacklist_collection.insert_one({'jti' : jti})
    return jsonify({'msg' : 'Logged out successfully!'}), 200

if __name__ == "__main__":
    app.run(debug=True)
    
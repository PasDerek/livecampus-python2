import bcrypt
from . import env
import datetime
import jwt

def hash_password(password):
    return bcrypt.hashpw(str.encode(password), env.secrets['salt'])

def check_hash_password(password, db_password):
    return bcrypt.checkpw(str.encode(password), db_password)

def generate_jwt(username):
    #Generation de token
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, env.secrets['Jwt'], algorithm='HS256')
    return token
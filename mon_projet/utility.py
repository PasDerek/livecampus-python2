import bcrypt
from . import env
import datetime
import jwt

def hash_password(password):
    return bcrypt.hashpw(str.encode(password), env.SECRETS['SALT'])

def generate_jwt(username):
    #Generation de token
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, env.SECRETS['JWT'], env.SECRETS['JWT_algo'])
    return token

def decode_jwt(token):
    payload = jwt.decode(token, env.SECRETS['JWT'], env.SECRETS['JWT_algo'])
    return payload
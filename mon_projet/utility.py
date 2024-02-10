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
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }
    token = jwt.encode(payload, env.SECRETS['JWT'], env.SECRETS['JWT_algo']).decode('utf-8')
    return token

def decode_jwt(token):
    payload = jwt.decode(token, env.SECRETS['JWT'], env.SECRETS['JWT_algo'])
    return payload
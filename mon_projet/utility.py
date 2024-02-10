import bcrypt
from . import env

def hash_password(password):
    return bcrypt.hashpw(str.encode(password), env.secrets['salt'])

def check_hash_password(password, db_password):
    return bcrypt.checkpw(str.encode(password), db_password)
from django.http import HttpResponse, HttpResponseRedirect
import bcrypt
from . import env
import datetime
import jwt

# Fonction hash de mot de passe (utilisé dans les models)
def hash_password(password):
    return bcrypt.hashpw(str.encode(password), env.SECRETS['SALT'])

# Fonction de génération de token JWT (utilisé dans la page de login étudiants)
def generate_jwt(username):
    # Payload = username + date d'expiration
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    # Token : payload + secret + algorithme 
    token = jwt.encode(payload, env.SECRETS['JWT'], env.SECRETS['JWT_algo']).decode('utf-8')
    return token

# Fonction de 'décodage' du token JWT (utilisé dans les pages de consultation étudiants)
def decode_jwt(token):
    try:
        payload = jwt.decode(token, env.SECRETS['JWT'], env.SECRETS['JWT_algo'])
        return payload
    except:
        reponse = HttpResponseRedirect('/login/')
        reponse.delete_cookie('JWT')
        return reponse
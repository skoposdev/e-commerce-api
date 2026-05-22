import datetime
import os

import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

def create_token(id: int):
    payload = {
        'id': id,
        'exp': datetime.datetime.now() + datetime.timedelta(minutes=30),
        'iat': datetime.datetime.now(),
    }

    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_jwt(token: str):
    try:
        print(token)
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'], options={'verify_iat': False})
    except jwt.ExpiredSignatureError:
        raise Exception('Signature expired. Please log in again.')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token. Please log in again.')
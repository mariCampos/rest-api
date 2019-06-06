import jwt
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64decode,b64encode
from settings import *


def generate_token(id):
       
    private_key = open('./../jwt-key').read()
    token = jwt.encode({'id': id}, private_key, algorithm='RS512').decode('utf-8')
    return token

def decode_token(token):
    public_key = open('./../jwt-key.pub').read()
    return jwt.decode(token, public_key, algorithms=['RS512'])
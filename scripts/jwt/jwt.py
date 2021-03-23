import jwt
import json
import scripts.secrets.secret as secret

KEY = secret.access_secret_version('JWTKey')


# Receives a dict with the user information and returns the  JWT
def generate_token(payload):
    # When no specified it uses hs256 as the protocol to generate the  toke
    enconded_jwt = jwt.encode(payload, KEY)
    return enconded_jwt

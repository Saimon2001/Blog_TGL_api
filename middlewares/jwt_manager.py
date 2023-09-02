from jwt import encode, decode

def create_token(data:dict):
    token: str = encode(payload=data, key='my_secrete_key', algorithm='HS256')
    return token

def validate_token(token: str) -> dict:
    algorithms = ["HS256"]
    data: dict = decode(token, key='my_secrete_key', algorithms=algorithms)
    return data

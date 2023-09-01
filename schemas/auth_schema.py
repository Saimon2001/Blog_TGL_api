from pydantic import BaseModel

class auth(BaseModel):
    email: str
    password: str
    
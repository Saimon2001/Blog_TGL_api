from pydantic import BaseModel

class Publication(BaseModel):
    publi_id: int
    user_id: int
    comment: str
    hastags: str
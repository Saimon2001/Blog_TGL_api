from pydantic import BaseModel

class Comments(BaseModel):
    comment_id: int
    publi_id: int
    user_id: int
    new_comment: str
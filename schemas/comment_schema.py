from pydantic import BaseModel

class Comment(BaseModel):
    comment_id: int
    user_id: int
    publication_id: int
    content: str
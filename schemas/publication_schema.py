from pydantic import BaseModel
from typing import Optional, List
from schemas.comment_schema import Comment

class Publication(BaseModel):
    publi_id: int
    user_id: int
    title: str
    content: str
    comments: List[Comment]
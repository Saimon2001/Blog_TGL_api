from fastapi import Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from typing import List
from middlewares.jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@TGL_blog.com":
            return HTTPException(status_code=403, detail="Credenciales no son validas")
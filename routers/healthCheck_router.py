from fastapi import APIRouter

health = APIRouter()


@health.get('/', tags= ['Healt check'])
def message():
    return "Health: checked ✅"
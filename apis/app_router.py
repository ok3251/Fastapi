from fastapi import APIRouter,HTTPException
from database import create_db_pool, close_db_pool, pool_query
from pydantic import BaseModel
page_router = APIRouter()


@page_router.on_event("startup")
async def startup_event():
    global Query
    page_router.db_pool = await create_db_pool()
    Query = page_router.db_pool 

@page_router.on_event("shutdown")
async def shutdown_event():
    await close_db_pool(page_router.db_pool)

@page_router.get("/")
async def main():
    try:
        name = '과니'
        # adduser = await pool_query(Query, "INSERT INTO user (user_name) VALUES (%s)", name)
        users = await pool_query(Query, "SELECT * FROM user")
        return {'body': users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



class Message(BaseModel):
    message:str
    name:str

@page_router.post("/about")
async def about(item:Message):
    print(item)
    return
import uvicorn
from fastapi import FastAPI, Depends
from app.db import database

app = FastAPI()

GET_ALL_USERS = """
    SELECT * FROM users;
"""

class BaseRepository:
    def __init__(self, db: database) -> None:
        self.db = db

class UsersRepository(BaseRepository):
    def __init__(self, db: database) -> None:
        super().__init__(db)
    
    async def get_all_users(self) -> []:
        users = await self.db.fetch_all(query=GET_ALL_USERS)
        return users

@app.on_event("startup")
async def startup():
    await database.connect()

@app.get("/")
def home():
    return {"home":"sweet home"}

@app.get('/users', status_code=200)
async def get_all_users():
    user_repo = UsersRepository(database)
    users = await user_repo.get_all_users()
    return {"users":users}

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


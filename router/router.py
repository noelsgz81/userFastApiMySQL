from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.user_schema import UserSchema
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash

user = APIRouter()

@user.get("/")
def root():
    return {"message" : "Fast API with router"}

@user.get("/api/user")
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        print(f"result0: {str(result)}")        
        result = ((s[0], s[1:]) for s in result)
        print(f"result1: {str(result)}")
        return {result}

@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    with engine.connect() as conn:
        new_user = data_user.dict()
        print(f"New_User: {str(new_user)}")
        new_user["user_password"] = generate_password_hash(data_user.user_password, "pbkdf2:sha256:30", 30)
        conn.execute(users.insert().values(new_user))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@user.put("/api/user")
def update_user():
    pass
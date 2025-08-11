from fastapi import APIRouter, Depends, HTTPException
from services.db_service import get_db_pool
from services.auth_service import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user,
)
from schemas.auth_schemas import SignupData, LoginData

router = APIRouter()

@router.post("/signup")
async def signup(data: SignupData, pool=Depends(get_db_pool)):
    print(f"[SIGNUP] Attempting signup for email={data.email} username={data.username}")
    async with pool.acquire() as conn:
        existing = await conn.fetchrow("SELECT * FROM blogschema.users WHERE email=$1", data.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_pw = hash_password(data.password)
        await conn.execute(
            "INSERT INTO blogschema.users (username, email, password_hash) VALUES ($1, $2, $3)",
            data.username, data.email, hashed_pw
        )
    return {"message": "User created successfully"}


@router.post("/login")
async def login(data: LoginData, pool=Depends(get_db_pool)):
    async with pool.acquire() as conn:
        user = await conn.fetchrow("SELECT * FROM blogschema.users WHERE email=$1", data.email)
        if not user or not verify_password(data.password, user["password_hash"]):
            raise HTTPException(status_code=400, detail="Invalid email or password")

        access_token = create_access_token(
            data={"user_id": user["id"], "email": user["email"]}
        )

        return {
            "message": "Login successful",
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
            },
        }


@router.get("/protected")
async def protected_route(current_user=Depends(get_current_user)):
    return {"message": f"Hello {current_user['email']}! This route is protected."}

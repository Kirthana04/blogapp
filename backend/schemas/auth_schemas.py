from pydantic import BaseModel, EmailStr

class SignupData(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginData(BaseModel):
    email: EmailStr
    password: str

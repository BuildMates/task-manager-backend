from pydantic import BaseModel, EmailStr


class SignupCommand(BaseModel):
    email: EmailStr
    password:str

from fastapi import APIRouter

from app.commands.signup_command import SignupCommand
from app.commands.login_command import LoginCommand
from app.queries.get_user_query import GetUserQuery
from app.services.auth_service import auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/signup")
def signup(command: SignupCommand):
    return auth_service.signup(command)


@router.post("/login")
def login(command: LoginCommand):
    return auth_service.login(command)


@router.get("/user")
def get_user(email: str):
    query = GetUserQuery(email=email)
    return auth_service.get_user(query)


@router.get("/users")
def get_all_users():
    return auth_service.get_all_users()
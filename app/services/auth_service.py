# app/services/auth_service.py

from fastapi import HTTPException

from app.commands.signup_command import SignupCommand
from app.commands.login_command import LoginCommand
from app.queries.get_user_query import GetUserQuery
from app.models.user_write_model import UserWriteModel
from app.repositories.user_repository import user_repository
from app.providers.user_data_provider import user_data_provider
from app.security.password import hash_password, verify_password


class AuthService:

#Write Operation
    def signup(self, command: SignupCommand):
        email = str(command.email).lower()

        existing_user = user_repository.get_user_for_login(email)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="User already exists"
            )

        password_hash = hash_password(command.password)

        user = UserWriteModel(
            email=email,
            password_hash=password_hash
        )

        user_repository.create_user(user)

        return {
            "message": "User created successfully",
            "user": {
                "email": user.email
            }
        }

    def login(self, command: LoginCommand):
        email = str(command.email).lower()

        user = user_repository.get_user_for_login(email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        is_password_valid = verify_password(
            plain_password=command.password,
            password_hash=user.password_hash
        )

        if not is_password_valid:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        read_user = user_data_provider.get_user_profile(email)

        return {
            "message": "Login successful",
            "user": {
                "email": read_user.email
            }
        }
    
#Read Operation
    def get_user(self, query: GetUserQuery):
        email = str(query.email).lower()

        user = user_data_provider.get_user_profile(email)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return {
            "email": user.email
        }

    def get_all_users(self):
        users = user_data_provider.get_all_user_profiles()

        return [
            {
                "email": user.email
            }
            for user in users
        ]


auth_service = AuthService()
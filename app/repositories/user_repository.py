from typing import Optional

from app.db.in_memory_database import users_db
from app.models.user_write_model import UserWriteModel


class UserRepository:

    def create_user(self, user: UserWriteModel):
        users_db[user.email] = user


    def get_user_for_login(self, email: str) -> Optional[UserWriteModel]:
        return users_db.get(email)


user_repository = UserRepository()
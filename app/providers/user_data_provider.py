from typing import List, Optional

from app.db.in_memory_database import users_db
from app.models.user_read_model import UserReadModel


class UserDataProvider:

        def get_user_profile(self, email: str) -> Optional[UserReadModel]:
            user = users_db.get(email)

            if not user:
                return None

            return UserReadModel(email=user.email)

        def get_all_user_profiles(self) -> List[UserReadModel]:
             return [UserReadModel(email=user.email)
                for user in users_db.values()]

user_data_provider = UserDataProvider()
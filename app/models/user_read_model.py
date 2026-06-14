# app/models/user_read_model.py

from dataclasses import dataclass


@dataclass
class UserReadModel:
    email: str
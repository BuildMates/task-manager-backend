# app/models/user_write_model.py

from dataclasses import dataclass


@dataclass
class UserWriteModel:
    email: str
    password_hash: str
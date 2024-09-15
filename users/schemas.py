from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import Path
from annotated_types import MinLen, MaxLen


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(2), MaxLen(21)]
    email: EmailStr

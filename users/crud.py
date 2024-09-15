from users.schemas import CreateUser


def create_user(user_input: CreateUser):
    user = user_input.model_dump()
    return {
        "message": "success",
        "user": user
    }

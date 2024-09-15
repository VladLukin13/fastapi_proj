from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn

app = FastAPI(
    title='Open gashtet'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'vlad'},
    {'id': 2, 'role': 'user', 'name': 'oly'},
    {'id': 3, 'role': 'peple', 'name': 'matvei'},
]


@app.get("/users/{user_name}")
def get_user(user_name: str):
    return [user for user in fake_users if user.get('name') == user_name]


@app.get("/{user_id}")
def get_user(user_id: int):
    for user in fake_users:
        if user.get('id') == user_id:
            return user.get("name")


@app.post("/users/{user_id}")
def change_new_name(user_id: int, new_name: str):
    current_user = [user for user in fake_users2 if user.get('id') == user_id][0]
    current_user['name'] = new_name
    return {'result': 200, 'date': current_user}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

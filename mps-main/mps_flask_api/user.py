from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

USER = {
    "1": {
        "user_name": "Julio Cesar Ferreira de Souza",
        "user_id": "1",
        "user_email": "Julio@gmail.com",
        "user_status": "0",
        "timestamp": get_timestamp(),
    },
    "2": {
        "user_name": "Lucas Cruz Araujo",
        "user_id": "2",
        "user_email": "Lucas@gmail.com",
        "user_status": "0",
        "timestamp": get_timestamp(),
    },
    "3": {
        "user_name": "Adriano Da Galera",
        "user_id": "3",
        "user_email": "Adriano@gmail.com",
        "user_status": "0",
        "timestamp": get_timestamp(),
    },
        "4": {
        "user_name": "Larissa Roque",
        "user_id": "4",
        "user_email": "Larissa@gmail.com",
        "user_status": "0",
        "timestamp": get_timestamp(),
    },
        "5": {
        "user_name": "Johann e Gabiru",
        "user_id": "5",
        "user_email": "Joharu@gmail.com",
        "user_status": "0",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(USER.values())


def create(user):
    user_id = user.get("user_id")
    user_name = user.get("user_name", "")
    user_email = user.get("user_email", "")
    user_status = user.get("user_status", "")

    if user_id and user_id not in USER:
        USER[user_id] = {
            "user_id": user_id,
            "user_name": user_name,
            "user_email": user_email,
            "user_status": user_status,
            "timestamp": get_timestamp(),
        }
        return USER[user_id], 201
    else:
        abort(
            406,
            f"User with last name {user_id} already exists",
        )


def read_one(user_id):
    if user_id in USER:
        return USER[user_id]
    else:
        abort(
            404, f"Person with ID {user_id} not found"
        )


def update(user_id, user):
    if user_id in USER:
        USER[user_id]["user_name"] = user.get("user_name", USER[user_id]["user_name"])
        USER[user_id]["user_status"] = user.get("user_status", USER[user_id]["user_status"])
        USER[user_id]["timestamp"] = get_timestamp()
        return USER[user_id]
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )


def delete(user_id):
    if user_id in USER:
        del USER[user_id]
        return make_response(
            f"{user_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )
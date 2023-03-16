from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

EVENT = {
    "1": {
        "event_id": "1",
        "event_title": "Evento 1",
        "event_description": "Essa é a descrição do evento 1",
        "event_date": "12/10/2000",
        "user_id": "1",
        "timestamp": get_timestamp(),
    },
    "2": {
        "event_id": "2",
        "event_title": "Evento 2",
        "event_description": "Essa é a descrição do evento 2",
        "event_date": "12/10/2000",
        "user_id": "1",
        "timestamp": get_timestamp(),
    },
    "3": {
        "event_id": "3",
        "event_title": "Evento 3",
        "event_description": "Essa é a descrição do evento 3",
        "event_date": "12/10/2000",
        "user_id": "2",
        "timestamp": get_timestamp(),
    },
    "4": {
        "event_id": "4",
        "event_title": "Evento 4",
        "event_description": "Essa é a descrição do evento 4",
        "event_date": "12/10/2000",
        "user_id": "2",
        "timestamp": get_timestamp(),
    },
    "5": {
        "event_id": "5",
        "event_title": "Evento 5",
        "event_description": "Essa é a descrição do evento 5",
        "event_date": "12/10/2000",
        "user_id": "3",
        "timestamp": get_timestamp(),
    },
    "6": {
        "event_id": "6",
        "event_title": "Evento 6",
        "event_description": "Essa é a descrição do evento 6",
        "event_date": "12/10/2000",
        "user_id": "3",
        "timestamp": get_timestamp(),
    },
    "7": {
        "event_id": "7",
        "event_title": "Evento 7",
        "event_description": "Essa é a descrição do evento 7",
        "event_date": "12/10/2000",
        "user_id": "4",
        "timestamp": get_timestamp(),
    },
    "8": {
        "event_id": "8",
        "event_title": "Evento 8",
        "event_description": "Essa é a descrição do evento 8",
        "event_date": "12/10/2000",
        "user_id": "4",
        "timestamp": get_timestamp(),
    },
    "9": {
        "event_id": "9",
        "event_title": "Evento 9",
        "event_description": "Essa é a descrição do evento 9",
        "event_date": "12/10/2000",
        "user_id": "4",
        "timestamp": get_timestamp(),
    },
    "10": {
        "event_id": "10",
        "event_title": "Evento 10",
        "event_description": "Essa é a descrição do evento 10",
        "event_date": "12/10/2000",
        "user_id": "5",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(EVENT.values())


def create(event):
    event_id = event.get("event_id")
    event_title = event.get("event_title", "")
    event_description = event.get("event_description", "")
    event_date = event.get("event_date", "")
    user_id = event.get("user_id")

    if event_id and event_id not in EVENT:
        EVENT[event_id] = {
            "event_id": event_id,
            "event_title": event_title,
            "event_description": event_description,
            "event_date": event_date,
            "user_id": user_id,
            "timestamp": get_timestamp(),
        }
        return EVENT[event_id], 201
    else:
        abort(
            406,
            f"User with last name {user_id} already exists",
        )


def read_one(event_id):
    if event_id in EVENT:
        return EVENT[event_id]
    else:
        abort(
            404, f"Person with ID {event_id} not found"
        )


def update(event_id, event):
    if event_id in EVENT:
        EVENT[event_id]["event_title"] = event.get("event_title", EVENT[event_id]["event_title"])
        EVENT[event_id]["event_description"] = event.get("event_description", EVENT[event_id]["event_description"])
        EVENT[event_id]["event_date"] = event.get("event_date", EVENT[event_id]["event_date"])
        EVENT[event_id]["timestamp"] = get_timestamp()
        return EVENT[event_id]
    else:
        abort(
            404,
            f"Person with ID {event_id} not found"
        )


def delete(event_id):
    if event_id in EVENT:
        del EVENT[event_id]
        return make_response(
            f"{event_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {event_id} not found"
        )
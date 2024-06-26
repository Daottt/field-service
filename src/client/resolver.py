import requests
import json

server_url = "http://127.0.0.1:8000"

def getAll(table: str) -> list:
    answer = requests.get(
        url=f'{server_url}/{table}/',
    )
    return answer.json()

def get_all_data(table:str):
    answer = requests.get(
        url=f'{server_url}/{table}/get_all_data',
    )
    return answer.json()

def get(table: str, _id: int):
    answer = requests.get(
        url=f'{server_url}/{table}/id',
        params={"object_id": _id}
    )
    return answer.json()

def create(table: str, model: dict):
    requests.post(
        url=f'{server_url}/{table}/create',
        data=json.dumps(model)
    )

def update(table: str, model: dict, index: int):
    requests.put(
        url=f'{server_url}/{table}/update',
        params={"object_id": index},
        data=json.dumps(model)
    )

def delete(table: str, index: int):
    requests.delete(
        url=f'{server_url}/{table}/delete',
        params={"object_id": index}
    )

def login(name: str, password: str):
    answer = requests.get(
        url=f'{server_url}/Users/login',
        params={"name": name, "password": password}
    )
    if not answer: return None
    return answer.json()

def get_fields(table: str):
    answer = requests.get(
        url=f'{server_url}/{table}/fields',
    )
    return answer.json()

def get_task_by_personal(personal_id: int):
    answer = requests.get(
        url=f'{server_url}/Task/get_by_personal/',
        params={"id": personal_id},
    )
    return answer.json()

def get_task_by_client(client_id: int):
    answer = requests.get(
        url=f'{server_url}/Task/get_by_client/',
        params={"id": client_id},
    )
    return answer.json()

def get_reviews(index):
    answer = requests.get(
        url=f'{server_url}/Reviews/get_by_personal/',
        params={"id": index},
    )
    return answer.json()

def add_comment(text,master,task):
    requests.post(
        url=f'{server_url}/Comments/create',
        data=json.dumps({"text": text, "master_id":master, "task_id":task})
    )

def get_comment(index):
    answer = requests.get(
        url=f'{server_url}/Comments/get_by_task/',
        params={"id": index},
    )
    return answer.json()

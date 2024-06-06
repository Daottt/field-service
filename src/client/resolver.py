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

from typing import Optional
from pydantic import BaseModel

class BaseModelModify(BaseModel):
    id: Optional[int] = None

class Post(BaseModelModify):
    name: str
    power_level: int

class Personal(BaseModelModify):
    fio: Optional[str] = None
    post_id: int

class Users(BaseModelModify):
    login: str
    password: str
    personal_id: Optional[int]

class ClientData(BaseModelModify):
    fio: Optional[str] = None
    address: str
    phone_number: Optional[str] = None

class TaskStatus(BaseModelModify):
    name: str

class TaskType(BaseModelModify):
    name: str

class Task(BaseModelModify):
    date_start: Optional[str] = None
    clientdata_id: int
    personal_id: Optional[int] = None
    taskstatus_id: Optional[int] = None
    tasktype_id: Optional[int] = None

class Reviews(BaseModelModify):
    text: Optional[str] = None
    client_id: Optional[int] = None
    master_id: Optional[int] = None

class Comments(BaseModelModify):
    text: Optional[str] = None
    master_id: Optional[int] = None
    task_id: Optional[int] = None

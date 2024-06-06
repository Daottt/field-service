from typing import Optional
from pydantic import BaseModel

class BaseModelModify(BaseModel):
    id: Optional[int] = None

class Post(BaseModelModify):
    name: str
    power_level: int

class Personal(BaseModelModify):
    name: Optional[str] = None
    surname: Optional[str] = None
    post_id: int

class Users(BaseModelModify):
    login: str
    password: str
    personal_id: Optional[int]

class ClientData(BaseModelModify):
    name: Optional[str] = None
    surname: Optional[str] = None
    address: str
    phone_number: Optional[str] = None

class TaskStatus(BaseModelModify):
    name: str

class TaskType(BaseModelModify):
    name: str

class Task(BaseModelModify):
    date_start: Optional[str] = None
    clientdata_id: int
    personal_id: Optional[int]
    taskstatus_id: Optional[int] = None
    tasktype_id: Optional[int] = None

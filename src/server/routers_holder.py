from .router import Router
from .resolver import Resolver
from .routers_resolvers.auth_router import AuthRouter
from .routers_resolvers.task_router import TaskRouter
from src.database.models import *

routers = (AuthRouter("Users", Users).router,
           TaskRouter("Task", Task).router,
           Router("TaskType", TaskType).router,
           Router("TaskStatus", TaskStatus).router,
           Router("Post", Post).router,
           Router("Personal", Personal).router,
           Router("ClientData", ClientData).router)

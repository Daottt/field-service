from .router import Router
from .resolver import Resolver
from .routers_resolvers.auth_router import AuthRouter
from .routers_resolvers.task_router import TaskRouter
from .routers_resolvers.personal_router import PersonalRouter
from .routers_resolvers.reviews_router import ReviewsRouter
from .routers_resolvers.comments_router import CommentsRouter
from src.database.models import *

routers = (AuthRouter("Users", Users).router,
           TaskRouter("Task", Task).router,
           Router("TaskType", TaskType).router,
           Router("TaskStatus", TaskStatus).router,
           Router("Post", Post).router,
           PersonalRouter("Personal", Personal).router,
           Router("ClientData", ClientData).router,
           CommentsRouter("Comments", Comments).router,
           ReviewsRouter("Reviews", Reviews).router)

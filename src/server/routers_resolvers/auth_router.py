from src.database.db_manager import db
from src.server.router import Router
from src.database.models import BaseModelModify

class AuthRouter(Router):
    def __init__(self, name, model: type[BaseModelModify]):
        super(AuthRouter, self).__init__(name, model)
        self.router.add_api_route('/login', login, methods=["get"])

def login(name: str, password: str):
    res = db.execute(
        query=f'select Users.id, Personal.id, Post.power_level from Users '
              f'join Personal ON Personal.id = Users.personal_id '
              f'join Post ON Personal.post_id = Post.id '
              f'where login=(?) and password =(?)',
        args=(name, password)
    )
    return {
        "UserID": res[0],
        "PersonalID": res[1],
        "PowerLevel": res[2]
    }

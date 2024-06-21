from src.database.db_manager import db
from src.server.router import Router
from src.database.models import BaseModelModify

class PersonalRouter(Router):
    def __init__(self, name, model: type[BaseModelModify]):
        super(PersonalRouter, self).__init__(name, model)
        self.router.add_api_route('/get_all_data', self.get_all_data, methods=["get"])
        self.router.add_api_route('/get_by_post/', self.get_by_post, methods=["get"])

    def get_all_data(self):
        return self.get_data()

    def get_by_post(self, id):
        return self.get_data(post_id=int(id))

    def get_data(self, post_id=0):
        query = (f'select Personal.id, Personal.fio, Post.* from Personal '
                 f'join Post ON Post.id = Personal.post_id ')

        if post_id > 0:
            query += f" where Personal.post_id = {post_id}"

        res_list = db.execute(query=query, many=True)
        return self.get_models(res_list)

    def get_models(self, res_list) -> list:
        models = []
        if res_list:
            for res in res_list:
                print(res)
                models.append({
                    "id": res[0],
                    "fio": res[1],
                    "post": (res[2], res[3], res[4])
                })
        return models

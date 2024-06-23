from src.database.db_manager import db
from src.server.router import Router
from src.database.models import BaseModelModify

class CommentsRouter(Router):
    def __init__(self, name, model: type[BaseModelModify]):
        super(CommentsRouter, self).__init__(name, model)
        self.router.add_api_route('/get_all_data', self.get_all_data, methods=["get"])
        self.router.add_api_route('/get_by_task/', self.get_by_task, methods=["get"])

    def get_all_data(self):
        return self.get_data()

    def get_by_task(self, id):
        return self.get_data(task=int(id))

    def get_data(self, task=0):
        query = (f'select Comments.id, Comments.text, Personal.* from Comments '
                 f'join Personal ON Comments.master_id = Personal.id ')

        if task > 0:
            query += f" where Comments.task_id = {task}"

        res_list = db.execute(query=query, many=True)
        return self.get_models(res_list)

    def get_models(self, res_list) -> list:
        models = []
        if res_list:
            for res in res_list:
                print(res)
                models.append({
                    "id": res[0],
                    "text": res[1],
                    "personal": (res[2], res[3], res[4])
                })
        return models
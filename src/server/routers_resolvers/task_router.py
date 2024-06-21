from src.database.db_manager import db
from src.server.router import Router
from src.database.models import BaseModelModify

class TaskRouter(Router):
    def __init__(self, name, model: type[BaseModelModify]):
        super(TaskRouter, self).__init__(name, model)
        # self.router.add_api_route('/get_data', get_data, methods=["get"])
        self.router.add_api_route('/get_all_data', self.get_all_data, methods=["get"])
        self.router.add_api_route('/get_by_personal/', self.get_by_personal, methods=["get"])
        self.router.add_api_route('/get_by_post/', self.get_by_post, methods=["get"])
        self.router.add_api_route('/get_by_client/', self.get_by_client, methods=["get"])

    def get_all_data(self):
        return self.get_data()

    def get_by_personal(self, id):
        return self.get_data(personal_id=int(id))

    def get_by_post(self, id):
        return self.get_data(post_id=int(id))

    def get_by_client(self, id):
        return self.get_data(client_id=int(id))

    def get_data(self, personal_id=0, post_id=0, client_id=0):
        query = (f'select Task.id, Task.date_start, ClientData.*, '
                 f'Personal.*, TaskStatus.*, TaskType.*  from Task '
                 f'join ClientData ON ClientData.id = Task.clientdata_id '
                 f'join Personal ON Personal.id = Task.personal_id '
                 f'join TaskStatus ON TaskStatus.id = Task.taskstatus_id '
                 f'join TaskType ON TaskType.id = Task.tasktype_id ')

        if personal_id > 0:
            query += f" where Personal.id = {personal_id} "

        if post_id > 0:
            query += f" where Personal.post_id = {post_id}"

        if client_id > 0:
            query += f" where Task.clientdata_id= {client_id}"

        res_list = db.execute(query=query, many=True)
        return self.get_models(res_list)

    def get_models(self, res_list) -> list:
        models = []
        if res_list:
            for res in res_list:
                print(res)
                models.append({
                    "id": res[0],
                    "date_start": res[1],
                    "clientdata": (res[2], res[3], res[4], res[5]),
                    "personal": (res[6], res[7], res[8]),
                    "taskstatus": (res[9], res[10]),
                    "tasktype": (res[11], res[12])
                })
        return models

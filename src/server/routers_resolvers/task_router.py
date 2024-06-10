from src.database.db_manager import db
from src.server.router import Router
from src.database.models import BaseModelModify

class TaskRouter(Router):
    def __init__(self, name, model: type[BaseModelModify]):
        super(TaskRouter, self).__init__(name, model)
        # self.router.add_api_route('/get_data', get_data, methods=["get"])
        self.router.add_api_route('/get_all_data', self.get_all_data, methods=["get"])
        self.router.add_api_route('/get_by_personal/', self.get_by_personal, methods=["get"])

    def get_all_data(self):
        res_list = db.execute(query=f'select Task.id, Task.date_start, ClientData.*, '
                                    f'Personal.*, TaskStatus.*, TaskType.*  from Task '
                                    f'join ClientData ON ClientData.id = Task.clientdata_id '
                                    f'join Personal ON Personal.id = Task.personal_id '
                                    f'join TaskStatus ON TaskStatus.id = Task.taskstatus_id '
                                    f'join TaskType ON TaskType.id = Task.tasktype_id ',
                              many=True)
        return self.get_models(res_list)

    def get_by_personal(self, id):
        res_list = db.execute(query=f'select Task.id, Task.date_start, ClientData.*, '
                                    f'Personal.*, TaskStatus.*, TaskType.*  from Task '
                                    f'join ClientData ON ClientData.id = Task.clientdata_id '
                                    f'join Personal ON Personal.id = Task.personal_id '
                                    f'join TaskStatus ON TaskStatus.id = Task.taskstatus_id '
                                    f'join TaskType ON TaskType.id = Task.tasktype_id '
                                    f'where Personal.id = {id}',
                              many=True)
        return self.get_models(res_list)

    def get_models(self, res_list) -> list:
        models = []
        if res_list:
            for res in res_list:
                models.append({
                    "id": res[0],
                    "date_start": res[1],
                    "clientdata": (res[2], res[3], res[4], res[5], res[6]),
                    "personal": (res[7], res[8], res[9], res[10]),
                    "taskstatus": (res[11], res[12]),
                    "tasktype": (res[13], res[14])
                })
        return models

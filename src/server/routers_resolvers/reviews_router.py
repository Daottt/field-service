from src.database.db_manager import db
from src.server.router import Router
from src.database.models import BaseModelModify

class ReviewsRouter(Router):
    def __init__(self, name, model: type[BaseModelModify]):
        super(ReviewsRouter, self).__init__(name, model)
        self.router.add_api_route('/get_all_data', self.get_all_data, methods=["get"])
        self.router.add_api_route('/get_by_personal/', self.get_by_personal, methods=["get"])

    def get_all_data(self):
        return self.get_data()

    def get_by_personal(self, id):
        return self.get_data(personal=int(id))

    def get_data(self, personal=0):
        query = (f'select Reviews.id, Reviews.text,ClientData.*, Personal.* from Reviews '
                 f'join Personal ON Reviews.master_id = Personal.id '
                 f'join ClientData ON Reviews.client_id = ClientData.id')

        if personal > 0:
            query += f" where Personal.id = {personal}"

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
                    "client": (res[5], res[6], res[7], res[8]),
                    "personal": (res[2], res[3], res[4])
                })
        return models
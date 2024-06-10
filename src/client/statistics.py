from PySide6.QtWidgets import QLabel, QListWidget
from src.client.resolver import getAll

def update_statistics(complete: QLabel, types: QListWidget):
    data = getAll("Task")
    complete.setText(f"Количество выполненных заявок: {complete_sum(data)}")
    types.clear()
    task_types(types, data)

def complete_sum(data: list):
    complete: int = 0
    for item in data:
        if item["taskstatus_id"] == 3:
            complete += 1
    return complete

def task_types(qlist: QListWidget, data: list):
    types: dict = {}
    tasks_type: dict = {}
    for item in getAll("TaskType"):
        tasks_type[item["id"]] = item["name"]

    for item in data:
        type = item['tasktype_id']
        if types.__contains__(type):
            types[type] += 1
        else:
            types[type] = 1
    for key, value in types.items():
        qlist.addItem(f"{tasks_type[key]}: {value}")

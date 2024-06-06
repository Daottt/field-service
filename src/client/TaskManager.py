from PySide6.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QMessageBox
from src.client.ui.ui_main import Ui_MainWindow
from src.client.ClientDataWindow import ClientDataWindow
from src.client.resolver import *
from src.database.models import Task

TableFields = ["Время начала работ", "ФИО клиента", "Адрес клиента",
               "ФИО работника", "Статус задачи", "Тип задачи"]

class TaskManager:
    def __init__(self, ui, window):
        self.ui: Ui_MainWindow = ui
        self.window = window
        self.Table: QTableWidget = self.ui.RequestsTable
        self.Add: QPushButton = self.ui.Add_R
        self.Update: QPushButton = self.ui.Update_R
        self.Delete: QPushButton = self.ui.Delete_R

        self.Add.clicked.connect(self.add_task)
        self.Update.clicked.connect(self.change_task)
        self.Delete.clicked.connect(self.delete_task)
        self.ui.client_data.clicked.connect(self.open_client_data)

        self.ui.create.clicked.connect(self.create_task)
        self.combo_box_data: list = list()
        self.ui.task_c_layout.setVisible(False)
        self.ui.start_date.setCalendarPopup(True)
        self.current_index: int = -1
        self.client_window = None

        self.create: bool = True
        self.raw_data: list = []
        self.client_data: list = []

    def set_combo_box_data(self):
        self.combo_box_data.clear()
        self.combo_box_data.append(self.set_combobox(self.ui.personal_box, "Personal"))
        self.combo_box_data.append(self.set_combobox(self.ui.status_box, "TaskStatus"))
        self.combo_box_data.append(self.set_combobox(self.ui.type_box, "TaskType"))
        self.ui.create.setEnabled(False)

    def add_task(self):
        self.set_combo_box_data()
        self.ui.create.setText("Создать")
        self.ui.task_c_layout.setVisible(True)
        self.create = True
        self.ui.create.setEnabled(True)

    def change_task(self):
        self.set_combo_box_data()
        self.ui.create.setText("Изменить")
        self.ui.task_c_layout.setVisible(True)
        self.create = False

        row = self.raw_data[self.Table.currentRow()]
        data: list = list(row.values())
        self.current_index = data[0]
        self.ui.start_date.setDateTime(self.ui.start_date.dateTimeFromText(data[1]))
        self.client_data = list(get("ClientData", data[2]).values())
        self.ui.label_2.setText(f"Клиент: ID:{data[2]}")
        self.ui.personal_box.setCurrentIndex(self.combo_box_data[0].index(data[3]))
        self.ui.status_box.setCurrentIndex(self.combo_box_data[1].index(data[4]))
        self.ui.type_box.setCurrentIndex(self.combo_box_data[2].index(data[5]))

        self.ui.create.setEnabled(True)

    def set_combobox(self, box: QComboBox, table_name: str, data_field: str = "name") -> list:
        box.clear()
        data = getAll(table_name)
        box_id = []
        text = list()
        for d in data:
            text.append(d[data_field])
            box_id.append(d["id"])
        box.addItems(text)
        return box_id

    def create_task(self):
        if self.create:
            create("Task", self.get_model())
            self.ui.task_c_layout.setVisible(False)
            self.UpdateTableData()
        else:
            update("Task", self.get_model(), self.current_index)
            self.ui.task_c_layout.setVisible(False)
            self.UpdateTableData()

    def delete_task(self):
        ret = QMessageBox.warning(self.window, "Подтверждение",
                                  f"Вы хотите удалить запись с id:{self.current_index}",
                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        if ret != QMessageBox.StandardButton.Yes:
            return

        delete("Task", self.current_index)

    def get_model(self) -> dict:
        box_data = list()
        box_data.append(self.ui.personal_box.currentIndex())
        box_data.append(self.ui.status_box.currentIndex())
        box_data.append(self.ui.type_box.currentIndex())
        values = list()
        values.append(0)
        values.append(self.ui.start_date.text())
        values.append(self.client_data[0])
        for i in range(len(box_data)):
            values.append(self.combo_box_data[i][box_data[i]])
        return dict(zip(Task.model_fields.keys(), values))

    def open_client_data(self):
        self.client_window = ClientDataWindow()
        self.client_window.ui.Select.clicked.connect(self.select_client)

    def select_client(self):
        self.client_data.clear()
        table: QTableWidget = self.client_window.ui.Table
        data = []
        for i in range(5):
            data.append(table.item(table.currentRow(), i).text())
        self.client_data = data
        self.ui.label_2.setText(f"Клиент: ID:{data[0]}")
        self.client_window.close()

    def UpdateTableData(self):
        self.raw_data.clear()
        table_name = "Task"
        self.Table = self.ui.RequestsTable
        self.Table.clear()
        self.Table.setColumnCount(len(TableFields))
        self.Table.setHorizontalHeaderLabels(TableFields)
        data = get_all_data(table_name)
        self.raw_data = getAll(table_name)
        self.Table.setRowCount(len(data))

        row_index = 0
        for values in data:
            self.Table.setItem(row_index, 0, QTableWidgetItem(str(values["date_start"])))
            self.Table.setItem(row_index, 1, QTableWidgetItem(str(values["clientdata"][1] + " " + values["clientdata"][2])))
            self.Table.setItem(row_index, 2, QTableWidgetItem(str(values["clientdata"][3])))
            self.Table.setItem(row_index, 3, QTableWidgetItem(str(values["personal"][1] + " " + values["personal"][2])))
            self.Table.setItem(row_index, 4, QTableWidgetItem(str(values["taskstatus"][1])))
            self.Table.setItem(row_index, 5, QTableWidgetItem(str(values["tasktype"][1])))
            row_index += 1

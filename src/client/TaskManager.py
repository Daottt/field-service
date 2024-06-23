from PySide6.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QMessageBox, QWidget
from src.client.ui.ui_main import Ui_MainWindow
from src.client.ClientDataWindow import ClientDataWindow
from src.client.ui.ui_table_window import Ui_Form
from src.client.resolver import *
from src.database.models import Task

TableFields = ["ID", "Время начала работ", "ФИО клиента", "Адрес клиента",
               "ФИО работника", "Статус задачи", "Тип задачи"]

comment_headers = ["ID", "Текст", "ФИО мастера"]

class TaskManager:
    def __init__(self, ui, window):
        self.ui: Ui_MainWindow = ui
        self.window = window
        self.Table: QTableWidget = self.ui.RequestsTable
        self.comments_widget = None
        self.Add: QPushButton = self.ui.Add_R
        self.Update: QPushButton = self.ui.Update_R
        self.Delete: QPushButton = self.ui.Delete_R

        self.Add.clicked.connect(self.add_task)
        self.Update.clicked.connect(self.change_task)
        self.Delete.clicked.connect(self.delete_task)
        self.ui.com_R.clicked.connect(self.show_comments)
        self.ui.client_data.clicked.connect(self.open_client_data)
        self.row_selection(False)
        self.ui.RequestsTable.currentItemChanged.connect(lambda: self.row_selection(True))

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
        self.combo_box_data.append(self.set_combobox(self.ui.personal_box, "Personal", "fio"))
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
            text.append(d[data_field]) #ПОЛЕ ИЗ КОТОРОГО БЕРЁТСЯ ТЕКСТ ДЛЯ BOX'а
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
        index = self.get_current_id()
        ret = QMessageBox.warning(self.window, "Подтверждение",
                                  f"Вы хотите удалить запись с id:{index}",
                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        if ret != QMessageBox.StandardButton.Yes:
            return
        delete("Task", index)
        self.UpdateTableData()

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
        for i in range(4):
            data.append(table.item(table.currentRow(), i).text())
        self.client_data = data
        self.ui.label_2.setText(f"Клиент: ID:{data[0]}")
        self.client_window.close()

    def row_selection(self, enabled):
        self.ui.Update_R.setEnabled(enabled)
        self.ui.Delete_R.setEnabled(enabled)
        self.ui.com_R.setEnabled(enabled)

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
            self.Table.setItem(row_index, 0, QTableWidgetItem(str(values["id"])))
            self.Table.setItem(row_index, 1, QTableWidgetItem(str(values["date_start"])))
            self.Table.setItem(row_index, 2, QTableWidgetItem(str(values["clientdata"][1])))
            self.Table.setItem(row_index, 3, QTableWidgetItem(str(values["clientdata"][2])))
            self.Table.setItem(row_index, 4, QTableWidgetItem(str(values["personal"][1])))
            self.Table.setItem(row_index, 5, QTableWidgetItem(str(values["taskstatus"][1])))
            self.Table.setItem(row_index, 6, QTableWidgetItem(str(values["tasktype"][1])))
            row_index += 1
        self.Table.resizeColumnsToContents()

    def get_current_id(self) -> int:
        index = self.Table.selectedIndexes()[0]
        return self.Table.model().data(index)

    def show_comments(self):
        self.comments_widget = QWidget()
        self.comments_widget.ui = Ui_Form()
        self.comments_widget.ui.setupUi(self.comments_widget)
        self.update_comment_data()
        self.comments_widget.show()
        self.comments_widget.ui.Add.setVisible(False)
        self.comments_widget.ui.Update.setVisible(False)
        self.comments_widget.ui.Delete.setVisible(False)

    def update_comment_data(self):
        table = self.comments_widget.ui.Table
        table.clear()
        table.setColumnCount(len(comment_headers))
        table.setHorizontalHeaderLabels(comment_headers)
        data = get_comment(self.get_current_id())
        table.setRowCount(len(data))

        row_index = 0
        for values in data:
            table.setItem(row_index, 0, QTableWidgetItem(str(values["id"])))
            table.setItem(row_index, 1, QTableWidgetItem(str(values["text"])))
            table.setItem(row_index, 2, QTableWidgetItem(str(values["personal"][1])))
            row_index += 1
        table.resizeColumnsToContents()

from PySide6.QtWidgets import QTableWidgetItem, QWidget
from src.client.ui.ui_main import Ui_MainWindow
from src.client.ui.ui_table_window import Ui_Form
from src.client.TableManager import TableManager
from src.client.resolver import *


headers = ["ID", "ФИО", "Адрес", "Номер телефона"]
story_headers = ["ID", "Время начала работ", "ФИО клиента", "Адрес клиента", "ФИО работника", "Тип задачи"]

class ClientManager:
    def __init__(self, ui, window):
        self.ui: Ui_MainWindow = ui
        self.window = window
        self.story_widget = None
        self.ui.client_table.currentItemChanged.connect(lambda: self.ui.client_story.setEnabled(True))
        self.ui.client_story.setEnabled(False)
        self.ui.client_story.clicked.connect(self.show_story)
        self.table_manager = TableManager(lambda: getAll("ClientData"), "ClientData", window, self.ui.client_table,
                                          self.ui.client_add, self.ui.client_update, self.ui.client_delete, headers)

    def get_current_id(self) -> int:
        index = self.ui.client_table.selectedIndexes()[0]
        return self.ui.client_table.model().data(index)

    def show_story(self):
        self.story_widget = QWidget()
        self.story_widget.ui = Ui_Form()
        self.story_widget.ui.setupUi(self.story_widget)
        self.update_story_data()
        self.story_widget.show()
        self.story_widget.ui.Add.setVisible(False)
        self.story_widget.ui.Update.setVisible(False)
        self.story_widget.ui.Delete.setVisible(False)

    def update_story_data(self):
        table = self.story_widget.ui.Table
        table.clear()
        table.setColumnCount(len(story_headers))
        table.setHorizontalHeaderLabels(story_headers)
        data = get_task_by_client(self.get_current_id())
        table.setRowCount(len(data))

        row_index = 0
        for values in data:
            table.setItem(row_index, 0, QTableWidgetItem(str(values["id"])))
            table.setItem(row_index, 1, QTableWidgetItem(str(values["date_start"])))
            table.setItem(row_index, 2, QTableWidgetItem(str(values["clientdata"][1])))
            table.setItem(row_index, 3, QTableWidgetItem(str(values["clientdata"][3])))
            table.setItem(row_index, 4, QTableWidgetItem(str(values["personal"][1])))
            table.setItem(row_index, 5, QTableWidgetItem(str(values["tasktype"][1])))
            row_index += 1
        table.resizeColumnsToContents()

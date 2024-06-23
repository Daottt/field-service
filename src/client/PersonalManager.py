from PySide6.QtWidgets import QTableWidgetItem, QWidget
from src.client.ui.ui_main import Ui_MainWindow
from src.client.ui.ui_table_window import Ui_Form
from src.client.DataWindow import DataWindow
from src.client.TableManager import TableManager
from src.client.resolver import *

headers = ["ID", "ФИО", "Должность"]
reviews_headers = ["ID", "Текст", "Клиент"]

class PersonalManager:
    def __init__(self, ui, window):
        self.ui: Ui_MainWindow = ui
        self.review_widget = None
        self.ui.personal_table.currentItemChanged.connect(lambda: self.ui.personal_rew.setEnabled(True))
        self.ui.personal_rew.setEnabled(False)
        self.ui.personal_rew.clicked.connect(self.show_reviews)
        #self.ui.personal_table.clicked.connect()
        self.table_manager = TableManager(lambda: getAll("Personal"), "Personal", window, self.ui.personal_table,
                                          self.ui.personal_add, self.ui.personal_update, self.ui.personal_delete, headers)
        self.story_widget = None

    def show_reviews(self):
        self.story_widget = QWidget()
        self.story_widget.ui = Ui_Form()
        self.story_widget.ui.setupUi(self.story_widget)
        self.update_reviews_data()
        self.story_widget.show()
        self.story_widget.ui.Add.clicked.connect(self.OpenNewWindow)

    def update_reviews_data(self):
        table = self.story_widget.ui.Table
        table.clear()
        table.setColumnCount(len(reviews_headers))
        table.setHorizontalHeaderLabels(reviews_headers)
        data = get_reviews(self.get_current_id())
        table.setRowCount(len(data))

        row_index = 0
        for values in data:
            table.setItem(row_index, 0, QTableWidgetItem(str(values["id"])))
            table.setItem(row_index, 1, QTableWidgetItem(str(values["text"])))
            table.setItem(row_index, 2, QTableWidgetItem(str(values["client"][2])))
            row_index += 1
        table.resizeColumnsToContents()

    def get_current_id(self) -> int:
        index = self.ui.personal_table.selectedIndexes()[0]
        return self.ui.personal_table.model().data(index)

    def OpenNewWindow(self):
        self.data_window = DataWindow("Reviews")
        self.data_window.ui.add.clicked.connect(self.add_data)
        self.data_window.ui.label.setText("Создать запись")
        self.data_window.ui.add.setText("Создать")

    def add_data(self):
        create("Reviews", self.get_model())
        self.update_reviews_data()

    def get_model(self) -> dict:
        values: list = self.data_window.GetData()
        self.data_window.close()
        print(dict(zip(get_fields("Reviews"), values)))
        return dict(zip(get_fields("Reviews"), values))

from PySide6.QtWidgets import QTableWidgetItem, QWidget
from src.client.ui.ui_main import Ui_MainWindow
from src.client.ui.ui_table_window import Ui_Form
from src.client.TableManager import TableManager
from src.client.resolver import *

headers = ["ID", "ФИО", "Должность"]

class PersonalManager:
    def __init__(self, ui, window):
        self.ui: Ui_MainWindow = ui
        self.review_widget = None
        self.ui.personal_table.currentItemChanged.connect(lambda: self.ui.client_story.setEnabled(True))
        self.ui.personal_rew.setEnabled(False)
        #self.ui.personal_table.clicked.connect()
        self.table_manager = TableManager(lambda: getAll("Personal"), "Personal", window, self.ui.personal_table,
                                          self.ui.personal_add, self.ui.personal_update, self.ui.personal_delete, headers)

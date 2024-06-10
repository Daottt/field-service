from PySide6.QtWidgets import QMainWindow
from src.client.ui.mobile import Ui_MainWindow
from src.client.resolver import get_task_by_personal, get

class MainWindow(QMainWindow):
    def __init__(self, user_data, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user_data = user_data
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton.setVisible(False)
        self.ui.pushButton_2.setVisible(False)
        #self.ui.pushButton.clicked.connect(self.tst)
        self.show_tasks()
        #print(get("Personal", self.user_data["PersonalID"]))

    def show_tasks(self):
        data = get_task_by_personal(self.user_data["PersonalID"])
        for i in data:
            print(i)

    def open_task(self):
        self.ui.stackedWidget.setCurrentIndex(1)

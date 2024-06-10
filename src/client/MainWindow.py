import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from src.client.ui.ui_main import Ui_MainWindow
from src.client.MobileWindow import MainWindow as Mobile
from src.client.TaskManager import TaskManager
from src.client.SettingsManager import SettingsManager
from src.client.resolver import login
from src.client.statistics import update_statistics

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.user_data = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.navButtons.setVisible(False)
        self.ui.LoginButton.clicked.connect(self.Login)
        self.ui.Log_out.clicked.connect(self.Logout)
        self.ui.ShowTables.clicked.connect(lambda: self.ChangeTab(1))
        self.ui.ShowSettings.clicked.connect(lambda: self.ChangeTab(2))
        self.ui.ShowStats.clicked.connect(lambda: self.ChangeTab(3))
        self.task_manger = TaskManager(self.ui, self)
        self.settings_tab = SettingsManager(self.ui, self)

    def Login(self):
        self.user_data = login(self.ui.loginText.text(), self.ui.passwordText.text())
        print(self.user_data)
        if not self.user_data:
            self.ui.loginInfo.setText("Неверный логин или пароль")
            return

        if self.user_data["PowerLevel"] == 1:
            window = Mobile(self.user_data)
            window.show()
            self.close()
            app = QApplication(sys.argv)
            sys.exit(app.exec())
            return

        self.ui.navButtons.setVisible(True)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.task_manger.UpdateTableData()

    def Logout(self):
        self.ui.ShowTables.setEnabled(False)
        self.ui.ShowSettings.setEnabled(True)
        self.ui.navButtons.setVisible(False)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.user_data = None

    def ChangeTab(self, tab_index):
        self.ui.ShowTables.setEnabled(True)
        self.ui.ShowSettings.setEnabled(True)
        self.ui.ShowStats.setEnabled(True)

        if tab_index == 1:
            self.task_manger.UpdateTableData()
            self.ui.ShowTables.setEnabled(False)
        if tab_index == 2:
            self.ui.ShowSettings.setEnabled(False)
        if tab_index == 3:
            self.ui.ShowStats.setEnabled(False)
            update_statistics(self.ui.SumText, self.ui.TaskTypes)

        self.ui.stackedWidget.setCurrentIndex(tab_index)

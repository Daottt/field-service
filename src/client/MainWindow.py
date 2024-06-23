import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from src.client.ui.ui_main import Ui_MainWindow
from src.client.MobileWindow import MainWindow as Mobile
from src.client.TaskManager import TaskManager
from src.client.ClientManager import ClientManager
from src.client.PersonalManager import PersonalManager
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
        self.ui.ShowClietns.clicked.connect(lambda: self.ChangeTab(4))
        self.ui.ShowPersonal.clicked.connect(lambda: self.ChangeTab(5))
        self.settings_tab = SettingsManager(self.ui, self)
        self.task_manger = TaskManager(self.ui, self)
        self.client_manager = ClientManager(self.ui, self)
        self.personal_manager = PersonalManager(self.ui, self)

    def Login(self):
        self.user_data = login(self.ui.loginText.text(), self.ui.passwordText.text())
        print(self.user_data)
        if not self.user_data:
            self.ui.loginInfo.setText("Неверный логин или пароль")
            return

        if self.user_data["PowerLevel"] == 2:
            window = Mobile(self.user_data)
            window.show()
            self.close()
            app = QApplication(sys.argv)
            sys.exit(app.exec())
            return
        if self.user_data["PowerLevel"] == 1:
            self.settings_tab.add_keys(2)
            self.ui.personal_add.setVisible(False)
            self.ui.personal_update.setVisible(False)
            self.ui.personal_delete.setVisible(False)
        if self.user_data["PowerLevel"] == 0:
            self.settings_tab.add_keys(0)
            self.ui.personal_add.setVisible(True)
            self.ui.personal_update.setVisible(True)
            self.ui.personal_delete.setVisible(True)

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
        self.ui.ShowClietns.setEnabled(True)
        self.ui.ShowPersonal.setEnabled(True)

        match tab_index:
            case 1:
                self.task_manger.UpdateTableData()
                self.ui.ShowTables.setEnabled(False)
                self.task_manger.row_selection(False)
                # self.ui.task_c_layout.setVisible(False)
            case 2:
                self.ui.ShowSettings.setEnabled(False)
            case 3:
                self.ui.ShowStats.setEnabled(False)
                update_statistics(self.ui.SumText, self.ui.TaskTypes)
            case 4:
                self.ui.ShowClietns.setEnabled(False)
                self.client_manager.table_manager.UpdateTableData()
            case 5:
                self.ui.ShowPersonal.setEnabled(False)
                self.personal_manager.table_manager.UpdateTableData()

        self.ui.stackedWidget.setCurrentIndex(tab_index)

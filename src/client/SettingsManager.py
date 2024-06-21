from PySide6.QtWidgets import QWidget
from src.client.ui.ui_main import Ui_MainWindow
from src.client.TableManager import TableManager
from src.client.resolver import *
from src.client.ui.ui_table_window import Ui_Form
# "название" : индекс в stacked_widget
Settings_Tabs = {"Приложение": 6, "Пользователи": 0, "Типы задач": 2, "Статусы задач": 3, "Должности": 4}
Settings_TabsM = {"Приложение": 6}

TablesList = ["Users", "Task", "ClientData", "Personal", "Post", "TaskStatus", "TaskType"]

class SettingsManager:
    def __init__(self, ui, window):
        self.ui: Ui_MainWindow = ui
        self.window = window

        settings_list = self.ui.SettingsList
        settings_list.clear()
        settings_list.currentRowChanged.connect(self.change_tab)
        if window.user_data["PowerLevel"] == 0:
            settings_list.addItems([item for item in Settings_Tabs.keys()])
        else:
            settings_list.addItems([item for item in Settings_TabsM.keys()])

        self.users = TableManager(lambda: (getAll("Users")), "Users", self.window,  self.ui.settings_table_5,
                                  self.ui.settings_add_5, self.ui.settings_update_5, self.ui.settings_delete_5)
        self.post = TableManager(lambda: (getAll("Post")), "Post", self.window,  self.ui.settings_table_7,
                                  self.ui.settings_add_7, self.ui.settings_update_7, self.ui.settings_delete_7)
        self.type = TableManager(lambda: (getAll("TaskType")), "TaskType", self.window,  self.ui.settings_table_8,
                                  self.ui.settings_add_8, self.ui.settings_update_8, self.ui.settings_delete_8)
        self.status = TableManager(lambda: (getAll("TaskStatus")), "TaskStatus", self.window,  self.ui.settings_table_9,
                                  self.ui.settings_add_9, self.ui.settings_update_9, self.ui.settings_delete_9)

        self.ui.settings_add_9.setVisible(False)
        self.ui.settings_delete_9.setVisible(False)

    def change_tab(self, index):
        tab = Settings_Tabs[self.ui.SettingsList.currentItem().text()]
        self.ui.stacked_Settings.setCurrentIndex(tab)
        match tab:
            case 0:
                self.users.UpdateTableData()
            case 2:
                self.type.UpdateTableData()
            case 3:
                self.status.UpdateTableData()
            case 4:
                self.post.UpdateTableData()

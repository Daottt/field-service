from src.client.ui.ui_main import Ui_MainWindow
from src.client.TableManager import TableManager
# "название" : индекс в stacked_widget
Settings_Tabs = {"Приложение": 6, "Пользователи": 0, "Персонал": 1, "Типы задач": 2, "Статусы задач": 3,
                 "Должности": 4, "Данные клиентов": 5}

TablesList = ["Users", "Task", "ClientData", "Personal", "Post", "TaskStatus", "TaskType"]

class SettingsManager:
    def __init__(self, ui, window):
        self.ui: Ui_MainWindow = ui
        self.window = window

        settings_list = self.ui.SettingsList
        settings_list.currentRowChanged.connect(self.change_tab)
        settings_list.addItems([item for item in Settings_Tabs.keys()])

        self.users = TableManager("Users", self.window,  self.ui.settings_table_5,
                                  self.ui.settings_add_5, self.ui.settings_update_5, self.ui.settings_delete_5)
        self.personal = TableManager("Personal", self.window,  self.ui.settings_table_10,
                                  self.ui.settings_add_10, self.ui.settings_update_10, self.ui.settings_delete_10)
        self.client_data = TableManager("ClientData", self.window,  self.ui.settings_table_6,
                                  self.ui.settings_add_6, self.ui.settings_update_6, self.ui.settings_delete_6)
        self.post = TableManager("Post", self.window,  self.ui.settings_table_7,
                                  self.ui.settings_add_7, self.ui.settings_update_7, self.ui.settings_delete_7)
        self.type = TableManager("TaskType", self.window,  self.ui.settings_table_8,
                                  self.ui.settings_add_8, self.ui.settings_update_8, self.ui.settings_delete_8)
        self.status = TableManager("TaskStatus", self.window,  self.ui.settings_table_9,
                                  self.ui.settings_add_9, self.ui.settings_update_9, self.ui.settings_delete_9)
        self.ui.settings_add_9.setVisible(False)
        self.ui.settings_delete_9.setVisible(False)

        self.ui.widget_debug.setVisible(False)
        self.task = TableManager("Task", self.window,  self.ui.settings_table_11,
                                  self.ui.settings_add_11, self.ui.settings_update_11, self.ui.settings_delete_11)

    def change_tab(self, index):
        tab = Settings_Tabs[self.ui.SettingsList.currentItem().text()]
        self.ui.stacked_Settings.setCurrentIndex(tab)
        match tab:
            case 0:
                self.users.UpdateTableData()
            case 1:
                self.personal.UpdateTableData()
            case 2:
                self.type.UpdateTableData()
            case 3:
                self.status.UpdateTableData()
            case 4:
                self.post.UpdateTableData()
            case 5:
                self.client_data.UpdateTableData()
            case 6: #TODO убрать
                self.task.UpdateTableData()

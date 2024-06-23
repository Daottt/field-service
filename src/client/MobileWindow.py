from PySide6.QtWidgets import QMainWindow, QWidget
from src.client.ui.mobile import Ui_MainWindow
from src.client.ui.mobile_task_data import Ui_Form
from src.client.resolver import get_task_by_personal, get, update, add_comment

class MainWindow(QMainWindow):
    def __init__(self, user_data, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.task_data = []
        self.user_data = user_data
        self.record = {}
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.pushButton.setVisible(False)
        self.ui.pushButton_2.setVisible(False)
        self.ui.add_comment.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.com_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.com_send.clicked.connect(self.create_comment)
                #self.ui.pushButton.clicked.connect(self.clear_layout)

        def back():
            self.show_tasks()
            self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Back.clicked.connect(back)
        self.show_tasks()
        #print(get("Personal", self.user_data["PersonalID"]))


    def create_comment(self):
        add_comment(self.ui.com_text.text(),self.user_data["PersonalID"], self.current_id)

    def show_tasks(self):
        self.clear_layout()
        self.task_data.clear()
        self.task_data = get_task_by_personal(self.user_data["PersonalID"])
        i = 0
        for item in self.task_data:
            widget = QWidget()
            widget.ui = Ui_Form()
            widget.ui.setupUi(widget)
            widget.ui.pushButton.setObjectName(str(i))
            widget.ui.pushButton.clicked.connect(self.open_task)
            i += 1
            widget.ui.TaskTime.setText(item["date_start"])
            widget.ui.Status.setText(item["taskstatus"][1])
            widget.ui.TaskType.setText(item["tasktype"][1])
            widget.ui.Address.setText(item["clientdata"][3])
            self.ui.scrollAreaWidgetContents.layout().addWidget(widget)

    def clear_layout(self):
        layout = self.ui.scrollAreaWidgetContents.layout()
        for i in reversed(range(layout.count())):
            layout.takeAt(i).widget().deleteLater()


    def open_task(self):
        sender = self.sender()
        data = self.task_data[int(sender.objectName())]
        record = get("Task", data["id"])
        self.current_id = record["id"]
        self.ui.Start_Complete.clicked.disconnect()

        def start():
            self.ui.Start_Complete.setText("Завершить")
            self.ui.Start_Complete.clicked.disconnect()
            self.ui.Start_Complete.clicked.connect(end)
            record["taskstatus_id"] = 2
            update("Task", record, record["id"])

        def end():
            self.ui.Start_Complete.setText("Завершена")
            self.ui.Start_Complete.setEnabled(False)
            record["taskstatus_id"] = 3
            update("Task", record, record["id"])

        print(record)
        match data["taskstatus"][0]:
            case 1:
                self.ui.Start_Complete.setEnabled(True)
                self.ui.Start_Complete.setText("Начать")
                self.ui.Start_Complete.clicked.connect(start)
            case 2:
                self.ui.Start_Complete.setText("Завершить")
                self.ui.Start_Complete.clicked.connect(end)
            case 3:
                self.ui.Start_Complete.setEnabled(False)
                self.ui.Start_Complete.setText("Завершена")

        self.ui.AddressText.setText(data["clientdata"][3])
        self.ui.time_text.setText(data["date_start"])
        self.ui.ClientText.setText(f'{data["clientdata"][1]} \n{data["clientdata"][2]}')
        self.ui.CallClient.setText(data["clientdata"][3])
        self.ui.Status.setText(f'Статус: {data["taskstatus"][1]}')
        self.ui.Type.setText(f'Тип: {data["tasktype"][1]}')
        self.ui.stackedWidget.setCurrentIndex(1)

from PySide6.QtWidgets import QDialog, QLineEdit, QComboBox, QDateTimeEdit
from PySide6.QtCore import QDateTime
from src.client.ui.ui_data import Ui_Dialog

TableFields = {"Users": [[QLineEdit, "Имя"], [QLineEdit, "Пароль"], [QLineEdit, "personal_id"]],
               "Task": [[QDateTimeEdit, "date_start"], [QLineEdit, "clientdata_id"], [QLineEdit, "personal_id"],
                        [QLineEdit, "taskstatus_id"],[QLineEdit, "tasktype_id"]],
               "ClientData": [[QLineEdit, "name"], [QLineEdit, "surname"], [QLineEdit, "address"],
                              [QLineEdit, "phone_number"]],
               "Post": [[QLineEdit, "Название"], [QLineEdit, "Доступ"]],
               "Personal": [[QLineEdit, "Имя"], [QLineEdit, "Фамилия"], [QLineEdit, "post_id"]],
               "TaskStatus": [[QLineEdit, "Название"]],
               "TaskType": [[QLineEdit, "Название"]]}

class DataWindow(QDialog):
    def __init__(self, table):
        super(DataWindow, self).__init__()
        self.table = table
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(lambda: self.close())
        self.createFields()
        self.show()

    def createFields(self):
        current_table = TableFields[self.table]
        for item in current_table:
            widget = item[0]()
            match widget:
                case QLineEdit():
                    widget.setPlaceholderText(item[1])
                case QComboBox():
                    widget.addItems(item[1])
                case QDateTimeEdit():
                    widget.setCalendarPopup(True)
                case _:
                    print("Виджет неизвестного типа")
                    return
            widget.setMinimumHeight(45)
            self.ui.DataContainer.addWidget(widget)

    def GetData(self) -> list:
        values: list = ['0']
        for layout_item in layout_widgets(self.ui.DataContainer):
            widget = layout_item.widget()
            values.append(get_data_from_widget(widget))
        return values

    def SetData(self, q_table):
        data: list = []
        index = q_table.selectedIndexes()
        for i in range(1, len(index)):
            data.append(q_table.model().data(index[i]))

        widgets: list = []
        for layout_item in layout_widgets(self.ui.DataContainer):
            widget = layout_item.widget()
            widgets.append(widget)
        for i in range(len(data)):
            set_data_for_widget(widgets[i], data[i])

def layout_widgets(layout):
    return (layout.itemAt(i) for i in range(layout.count()))

def set_data_for_widget(widget, data):
    match widget:
        case QLineEdit(): widget.setText(data)
        case QComboBox(): widget.setCurrentIndex(int(data))
        case QDateTimeEdit(): widget.setDateTime(QDateTime.fromString(data))
        case _: print("Виджет неизвестного типа")

def get_data_from_widget(widget):
    match widget:
        case QLineEdit(): return widget.text()
        case QComboBox(): return widget.currentIndex()
        case QDateTimeEdit(): return widget.text()
        case _: print("Виджет неизвестного типа")

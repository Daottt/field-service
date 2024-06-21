from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox, QPushButton
from src.client.DataWindow import DataWindow
from src.client.resolver import *

class TableManager:
    def __init__(self, data_func: callable, table_name: str, window, table: QTableWidget,
                 add_b: QPushButton, update_b: QPushButton, delete_b: QPushButton, headers: list = None):

        self.window = window
        self.table_name = table_name
        self.get_data = data_func
        self.current_table_keys = get_fields(table_name)
        self.data_window = None
        self.headers = headers

        self.Table: QTableWidget = table
        self.Add: QPushButton = add_b
        self.Update: QPushButton = update_b
        self.Delete: QPushButton = delete_b

        self.row_selection(False)
        self.Table.currentItemChanged.connect(lambda: self.row_selection(True))
        self.Add.clicked.connect(lambda: self.OpenNewWindow(True))
        self.Update.clicked.connect(lambda: self.OpenNewWindow(False))
        self.Delete.clicked.connect(self.delete_data)

        self.UpdateTableData()

    def UpdateTableData(self):
        table = self.Table
        table.clear()
        table.setColumnCount(len(self.current_table_keys))
        if not self.headers:
            table.setHorizontalHeaderLabels(self.current_table_keys)
        else:
            table.setHorizontalHeaderLabels(self.headers)
        data = self.get_data()

        table.setRowCount(len(data))
        table.setColumnWidth(0, 60)
        row_index = 0
        for values in data:
            for item in values.values():
                for i in range(len(data[0])):
                    table.setItem(i, row_index, QTableWidgetItem(str(item)))
                row_index += 1
        table.resizeColumnsToContents()
        self.row_selection(False)

    def row_selection(self, enabled):
        self.Update.setEnabled(enabled)
        self.Delete.setEnabled(enabled)

    def OpenNewWindow(self, add: bool):
        self.data_window = DataWindow(self.table_name)

        if add:
            self.data_window.ui.add.clicked.connect(self.add_data)
            self.data_window.ui.label.setText("Создать запись")
            self.data_window.ui.add.setText("Создать")
        else:
            self.data_window.SetData(self.Table)
            self.data_window.ui.add.clicked.connect(self.update_data)
            self.data_window.ui.label.setText("Обновить запись")
            self.data_window.ui.add.setText("Обновить")

    def get_model(self) -> dict:
        values: list = self.data_window.GetData()
        self.data_window.close()
        print(dict(zip(self.current_table_keys, values)))
        return dict(zip(self.current_table_keys, values))

    def get_current_id(self) -> int:
        index = self.Table.selectedIndexes()[0]
        return self.Table.model().data(index)

    def add_data(self):
        create(self.table_name, self.get_model())
        self.UpdateTableData()

    def update_data(self):
        update(self.table_name, self.get_model(), self.get_current_id())
        self.UpdateTableData()

    def delete_data(self):
        ret = QMessageBox.warning(self.window, "Подтверждение", f"Вы хотите удалить запись с id:{self.get_current_id()}",
                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        if ret != QMessageBox.StandardButton.Yes:
            return

        delete(self.table_name, self.get_current_id())
        self.UpdateTableData()



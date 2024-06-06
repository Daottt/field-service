from PySide6.QtWidgets import QDialog
from src.client.ui.ui_client_data import Ui_Dialog
from src.client.TableManager import TableManager

class ClientDataWindow(QDialog):
    def __init__(self):
        super(ClientDataWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.table = TableManager("ClientData", self, self.ui.Table, self.ui.Add, self.ui.Update, self.ui.Delete)
        self.row_selection(False)
        self.ui.Table.currentItemChanged.connect(lambda: self.row_selection(True))
        self.show()

    def row_selection(self, enabled):
        self.ui.Update.setEnabled(enabled)
        self.ui.Delete.setEnabled(enabled)
        self.ui.Select.setEnabled(enabled)

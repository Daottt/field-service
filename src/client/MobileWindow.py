from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, ui, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = ui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class BMainWindow(QMainWindow):
    def __init__(self, parent=None, status_bar: bool = True):
        super(BMainWindow, self).__init__(parent=parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        if status_bar:
            self.status_bar = QStatusBar()
            self.setStatusBar(self.status_bar)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            self.close()

    def b_show(self, show_maximized: bool = False, center_window: bool = True):
        if show_maximized:
            self.showMaximized()
        else:
            self.show()
            if center_window:
                self.b_center_window()

    def b_center_window(self):
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def display_message_statusbar(self, message: str, duration=5000):
        if hasattr(self, 'status_bar'):
            self.status_bar.showMessage(message=message, msecs=duration)

    def show_info_message(self, title: str = '', message: str = None):
        if message is not None:
            QMessageBox.information(self, title, message, QMessageBox.Ok)

    def show_error_message(self, title: str = 'Erro', message: str = None, txt: QLineEdit = None):
        if message is not None:
            QMessageBox.critical(self, title, message, QMessageBox.Ok)
            if txt is not None:
                txt.setFocus()

    def show_question_message(self, title: str = 'Erro', message: str = None):
        if message is not None:
            return QMessageBox.question(self, title, message, QMessageBox.Yes | QMessageBox.No)

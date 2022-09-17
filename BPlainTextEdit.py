from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class BPlainTextEdit(QPlainTextEdit):
    def __init__(self,
                 parent=None,
                 max_width: int = None, min_width: int = None,
                 max_height: int = None, min_height: int = None,
                 tab_focus: bool = True):
        super(BPlainTextEdit, self).__init__(parent=parent)

        if max_width is not None:
            self.setMaximumWidth(max_width)

        if min_width is not None:
            self.setMinimumWidth(min_width)

        if max_height is not None:
            self.setMaximumHeight(max_height)

        if min_height is not None:
            self.setMinimumHeight(min_height)

        self.setTabChangesFocus(tab_focus)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class BPushButton(QPushButton):
    def __init__(self,
                 text: str,
                 max_width: int = None, min_width: int = None,
                 max_height: int = None, min_height: int = None,
                 disabled: bool = False,
                 tool_tip: str = None):
        super(BPushButton, self).__init__(text=text)

        self.setDisabled(disabled)

        if max_width is not None:
            self.setMaximumWidth(max_width)

        if min_width is not None:
            self.setMinimumWidth(min_width)

        if max_height is not None:
            self.setMaximumHeight(max_height)

        if min_height is not None:
            self.setMinimumHeight(min_height)

        if tool_tip is not None:
            self.setToolTip(tool_tip)

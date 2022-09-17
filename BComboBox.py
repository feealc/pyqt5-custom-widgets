from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class BComboBox(QComboBox):
    def __init__(self,
                 parent=None,
                 max_width: int = None, min_width: int = None,
                 max_height: int = None, min_height: int = None,
                 disabled: bool = False):
        super(BComboBox, self).__init__(parent=parent)

        self.setDisabled(disabled)

        if max_width is not None:
            self.setMaximumWidth(max_width)

        if min_width is not None:
            self.setMinimumWidth(min_width)

        if max_height is not None:
            self.setMaximumHeight(max_height)

        if min_height is not None:
            self.setMinimumHeight(min_height)

    def b_clear_and_set_items(self, items_value: list = None, set_first_item: bool = True):
        if items_value is None:
            items_value = []

        self.clear()
        self.addItems(items_value)
        if len(items_value) > 0:
            if set_first_item is True:
                self.setCurrentIndex(0)
            else:
                self.setCurrentIndex(-1)

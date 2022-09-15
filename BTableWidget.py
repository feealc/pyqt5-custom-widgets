from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class BTableWidget(QTableWidget):
    def __init__(self, select_full_row=True, resize_to_content=True, hide_vertical_headers=True):
        super(BTableWidget, self).__init__()
        self.__center_content = False
        self.__header_labels: list[str] = []
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

        if select_full_row:
            self.b_select_full_row()

        if resize_to_content:
            self.b_ajust_header_columns()

        if hide_vertical_headers:
            self.b_hide_vertical_headers()

    def b_clear_content(self):
        self.clearContents()
        self.setRowCount(0)

    def b_select_full_row(self):
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def b_add_row(self, content_tuple: tuple):
        row = self.rowCount()
        self.setRowCount(row + 1)
        col = 0
        for item in content_tuple:
            cell = QTableWidgetItem(str(item))
            if self.__center_content:
                cell.setTextAlignment(Qt.AlignCenter)
            self.setItem(row, col, cell)
            col += 1

    def b_set_column_header(self, header_labels: list[str], ajust_colums: bool = False):
        self.__header_labels = header_labels
        self.setColumnCount(len(self.__header_labels))
        self.setHorizontalHeaderLabels(self.__header_labels)
        if ajust_colums:
            self.b_ajust_header_columns()

    def b_set_center_content(self, flag: bool = True):
        self.__center_content = flag

    def b_hide_vertical_headers(self):
        self.verticalHeader().setVisible(False)

    def b_show_vertical_headers(self):
        self.verticalHeader().setVisible(True)

    def b_ajust_header_columns(self, value: QHeaderView.ResizeMode = QHeaderView.ResizeToContents):
        header = self.horizontalHeader()
        for index, _ in enumerate(self.__header_labels):
            header.setSectionResizeMode(index, value)

    def b_ajust_header_columns_header_view(self, header_view_list):
        if len(header_view_list) != len(self.__header_labels):
            return
        header = self.horizontalHeader()
        for index, header_view in enumerate(header_view_list):
            header.setSectionResizeMode(index, header_view)

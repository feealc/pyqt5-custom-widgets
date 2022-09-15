# pyqt5-custom-widgets

Custom PyQt5 widgets to use in my projects

## BMainWindow
### Example
```python
class MyTestWindow(BMainWindow):
    def __init__(self):
        super(MyTestWindow, self).__init__(parent=None)
```

## BTableWidget
### Example
```python
# init object
table = BTableWidget()

# set headers
table.b_set_column_header(['Col 1', 'Col 2', 'Col 3'])

# add row
table.b_add_row(('val 1', 'val 2', 'val 3'))

# ajust headers sizes
table.b_ajust_header_columns_headerview(header_view_list=[QHeaderView.Stretch,
                                                          QHeaderView.ResizeToContents,
                                                          QHeaderView.ResizeToContents])

# double clicked action
table.doubleClicked.connect()
```

### Double clicked action
```python
def action_table_double_clicked(mi: QModelIndex):
    index = mi.row()
    if index > 0:
        pass
```

# System library imports
from PyEELS.external.qt import QtGui

class SeriesListWidget(QtGui.QListView):
    def __init__(self, model):
        super(SeriesListWidget, self).__init__()

        self.setModel(model)
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

    def add_series(self, name):
        item = QtGui.QStandardItem(name)
        self.model().appendRow(item)

    def clear(self):
        self.model().clear()

    def get_selected(self):
        if self.selectionModel().hasSelection():
            return [self.model().itemFromIndex(index).text() 
                    for index in self.selectionModel().selectedRows()]
        else:
            return []

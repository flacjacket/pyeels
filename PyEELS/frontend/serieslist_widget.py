# System library imports
from PyEELS.external.qt import QtGui, QtCore

class SeriesListWidget(QtGui.QListView):
    def __init__(self, model):
        super(SeriesListWidget, self).__init__()
        
        self.setModel(model)

    def add_series(self, name):
        item = QtGui.QStandardItem(name)
        #item.setCheckState(QtCore.Qt.Unchecked)
        #item.setCheckable(True)
        self.model().appendRow(item)

    def get_selected(self):
        if self.selectionModel().hasSelection():
            #print self.selectionModel().selectedRows()
            #print self.selectionModel().selectedRows().__class__
            return [self.model().itemFromIndex(index).text() 
                    for index in self.selectionModel().selectedRows()]
        else:
            return []

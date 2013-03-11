# System library imports
from PyEELS.external.qt import QtGui, QtCore

# Local imports
from PyEELS.frontend.plot_widget import PlotWidget

class MainWindow(QtGui.QMainWindow):
    def __init__(self, app, confirm_exit=True):
        super(MainWindow, self).__init__()
        self._app = app

        self.series_list_model = QtGui.QStandardItemModel()

    def init_main_frame(self):
        self.main_frame = QtGui.QWidget()

        self.plot = PlotWidget()
        #self.series_list = SeriesListWidget()

        self.series_list_view = QtGui.QListView()
        self.series_list_view.setModel(self.series_list_model)

        left_vbox = QtGui.QVBoxLayout()
        left_vbox.addWidget(self.series_list_view)
        left_vbox.addStretch(1)

        right_vbox = QtGui.QVBoxLayout()
        right_vbox.addWidget(self.plot)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(left_vbox, 3)
        hbox.addLayout(right_vbox, 1)

        self.main_frame.setLayout(hbox)

        self.setCentralWidget(self.main_frame)

    def init_status_bar(self):
        pass

    def init_menu_bar(self):
        pass

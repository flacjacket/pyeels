# System library imports
from PyEELS.external.qt import QtGui, QtCore

# Local imports
from PyEELS.frontend.plot_widget import PlotWidget
from PyEELS.frontend.serieslist_widget import SeriesListWidget

class MainWindow(QtGui.QMainWindow):
    def __init__(self, app, data, confirm_exit=True):
        super(MainWindow, self).__init__()
        self._app = app
        self.dataset = data

        self.series_list_model = QtGui.QStandardItemModel()

    def init_main_frame(self):
        self.main_frame = QtGui.QWidget()

        self.plot = PlotWidget()
        self.series_list = SeriesListWidget(self.series_list_model)

        self.load_button = QtGui.QPushButton("&Load")
        self.connect(self.load_button, QtCore.SIGNAL('clicked()'), self.load_file)

        left_vbox = QtGui.QVBoxLayout()
        left_vbox.addWidget(self.series_list)
        left_vbox.addWidget(self.load_button)
        left_vbox.addStretch(1)

        right_vbox = QtGui.QVBoxLayout()
        right_vbox.addWidget(self.plot)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(left_vbox, 1)
        hbox.addLayout(right_vbox, 3)

        self.main_frame.setLayout(hbox)

        self.setCentralWidget(self.main_frame)

    def init_status_bar(self):
        pass

    def init_menu_bar(self):
        pass

    def load_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,
                'Open a data file', '.', 'DAT files (*.dat);;All files (*.*)')

        if filename:
            name = self.dataset.load_data(str(filename))

            item = QtGui.QStandardItem(name)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setCheckable(True)
            self.series_list_model.appendRow(item)
            #self.series_list.add_series(name)

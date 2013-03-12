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
        self.series_list.setFixedWidth(200)
        self.connect(self.series_list.selectionModel(),
                QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'),
                self.update_plot)

        self.load_button = QtGui.QPushButton('&Load')
        self.connect(self.load_button,
                QtCore.SIGNAL('clicked()'),
                self.load_file)

        left_vbox = QtGui.QVBoxLayout()
        left_vbox.addWidget(self.series_list)
        left_vbox.addWidget(self.load_button)
        left_vbox.addStretch(1)

        right_vbox = QtGui.QVBoxLayout()
        right_vbox.addWidget(self.plot)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(left_vbox)
        hbox.addLayout(right_vbox)

        self.main_frame.setLayout(hbox)

        self.resize(800, 600)
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
            self.series_list.add_series(name)

    def update_plot(self):
        names = self.series_list.get_selected()
        self.plot.clear()

        for i, name in enumerate(names):
            data = self.dataset.get_data(str(name))
            self.plot.addPlot(name, data, i)
        self.plot.replot()


class Spy(QtCore.QObject):
    def __init__(self, parent):
        super(Spy, self).__init__(self)
        parent.setMouseTracking(True)
        parent.installEventFilter(self)

    def eventFilter(self, _, event):
        if event.type() == QEvent.MouseMove:
            self.emit(SIGNAL('MouseMove'), event.pos())
        return False

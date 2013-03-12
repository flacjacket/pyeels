# System library imports
from PyEELS.external.qt import QtGui, QtCore
from PyEELS.external.qwt import Qwt

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
        self.connect(Spy(self.plot.canvas()),
                QtCore.SIGNAL('MouseMove'),
                self.update_coordinates)

        self.series_list = SeriesListWidget(self.series_list_model)
        self.series_list.setFixedWidth(200)
        self.connect(self.series_list.selectionModel(),
                QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'),
                self.update_plot)

        self.load_button = QtGui.QPushButton('&Load')
        self.connect(self.load_button,
                QtCore.SIGNAL('clicked()'),
                self.load_file)

        self.x_label = QtGui.QLabel('x = ')
        self.y_label = QtGui.QLabel('y = ')
        xy_vbox = QtGui.QVBoxLayout()
        xy_vbox.addWidget(self.x_label)
        xy_vbox.addWidget(self.y_label)

        left_vbox = QtGui.QVBoxLayout()
        left_vbox.addWidget(self.series_list)
        left_vbox.addWidget(self.load_button)
        left_vbox.addStretch(1)
        left_vbox.addLayout(xy_vbox)

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

    def update_coordinates(self, position):
        self.x_label.setText('x = %6.1f' % self.plot.invTransform(Qwt.QwtPlot.xBottom, position.x()))
        self.y_label.setText('y = %6.1f' % self.plot.invTransform(Qwt.QwtPlot.yLeft, position.y()))

    def update_plot(self):
        names = self.series_list.get_selected()
        self.plot.clear()

        for i, name in enumerate(names):
            data = self.dataset.get_data(str(name))
            self.plot.addPlot(name, data, i)
        self.plot.replot()


class Spy(QtCore.QObject):
    def __init__(self, parent):
        super(Spy, self).__init__(parent)
        parent.setMouseTracking(True)
        parent.installEventFilter(self)

    def eventFilter(self, _, event):
        if event.type() == QtCore.QEvent.MouseMove:
            self.emit(QtCore.SIGNAL('MouseMove'), event.pos())
        return False

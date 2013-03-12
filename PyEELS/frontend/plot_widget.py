# System library imports
from PyEELS.external.qwt import Qwt
from PyEELS.external.qt import QtCore, QtGui

# Local imports
from PyEELS.frontend.picker import Picker

_colors = [QtCore.Qt.blue,
           QtCore.Qt.green,
           QtCore.Qt.red,
           QtCore.Qt.magenta,
           QtCore.Qt.cyan,
           QtCore.Qt.gray,
           QtCore.Qt.yellow,
           QtCore.Qt.darkBlue,
           QtCore.Qt.darkGreen,
           QtCore.Qt.darkRed,
           QtCore.Qt.darkMagenta,
           QtCore.Qt.darkCyan,
           QtCore.Qt.darkGray,
           QtCore.Qt.darkYellow]

class PlotWidget(Qwt.QwtPlot):
    def __init__(self, *args):
        super(PlotWidget, self).__init__()
        self.setCanvasBackground(QtCore.Qt.white)

        legend = Qwt.QwtLegend()
        legend.setItemMode(Qwt.QwtLegend.ClickableItem)
        self.insertLegend(legend, Qwt.QwtPlot.BottomLegend)

        self.picker = Picker(self.canvas())
        self.connect(self.picker,
                QtCore.SIGNAL('MouseMoved(const QMouseEvent&)'),
                self.onMouseMoved)
        self.connect(self.picker,
                QtCore.SIGNAL('MousePressed(const QMouseEvent&)'),
                self.onMousePressed)
        self.connect(self.picker,
                QtCore.SIGNAL('MouseReleased(const QMouseEvent&)'),
                self.onMouseReleased)
        self.connect(self.picker,
                QtCore.SIGNAL('PanningSignal'),
                self.onPanningSignal)
        self.picker.setSelectionFlags(Qwt.QwtPicker.DragSelection |
                Qwt.QwtPicker.RectSelection)

        self.picker.setRubberBand(Qwt.QwtPicker.NoRubberBand)
        self.picker.setRubberBandPen(QtGui.QPen(QtCore.Qt.green))
        self.picker.setEnabled(1)

        self._zoomStack = []

    def onMouseMoved(self, event):
        pass

    def onMousePressed(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._xpos = event.pos().x()
            self._ypos = event.pos().y()

            self.picker.setRubberBand(Qwt.QwtPicker.RectRubberBand)

    def onMouseReleased(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            xmin0 = min(self._xpos, event.pos().x())
            xmax0 = max(self._xpos, event.pos().x())
            ymin0 = min(self._ypos, event.pos().y())
            ymax0 = max(self._ypos, event.pos().y())

            xmin = self.invTransform(Qwt.QwtPlot.xBottom, xmin0)
            xmax = self.invTransform(Qwt.QwtPlot.xBottom, xmax0)
            ymin = self.invTransform(Qwt.QwtPlot.yLeft, ymax0)
            ymax = self.invTransform(Qwt.QwtPlot.yLeft, ymin0)

            xmin_graph, xmax_graph = self.getAxisLimits(Qwt.QwtPlot.xBottom)
            ymin_graph, ymax_graph = self.getAxisLimits(Qwt.QwtPlot.yLeft)

            xmin = max(xmin, xmin_graph)
            xmax = min(xmax, xmax_graph)
            ymin = max(ymin, ymin_graph)
            ymax = min(ymax, ymax_graph)

            self.setAxisScale(Qwt.QwtPlot.xBottom, xmin, xmax)
            self.setAxisScale(Qwt.QwtPlot.yLeft, ymin, ymax)
            self.replot()

            self._zoomStack.append((xmin_graph, xmax_graph, ymin_graph, ymax_graph))
            self.picker.setRubberBand(Qwt.QwtPicker.NoRubberBand)
        elif event.button() == QtCore.Qt.RightButton:
            if len(self._zoomStack):
                xmin, xmax, ymin, ymax = self._zoomStack.pop()
                self.setAxisScale(Qwt.QwtPlot.xBottom, xmin, xmax)
                self.setAxisScale(Qwt.QwtPlot.yLeft, ymin, ymax)
                self.replot()

    def onPanningSignal(self, ddict):
        pass

    def getAxisLimits(self, axis):
        xmin = self.canvasMap(axis).s1()
        xmax = self.canvasMap(axis).s2()
        return xmin, xmax

    def addPlot(self, series, data, index=0):
        color = QtGui.QColor(_colors[index % len(_colors)])

        curve = Qwt.QwtPlotCurve(series)
        pen = QtGui.QPen(color)
        pen.setWidth(2)
        curve.setPen(pen)
        curve.setData(data[:,0], data[:,1])

        curve.setSymbol(Qwt.QwtSymbol(Qwt.QwtSymbol.Ellipse,
            QtGui.QBrush(color),
            QtGui.QPen(color),
            QtCore.QSize(5,5)))

        curve.attach(self)
        self.replot()

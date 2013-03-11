# System library imports
from PyEELS.external.qwt import Qwt
from PyEELS.external.qt import QtCore

class Picker(Qwt.QwtPicker):
    def __init__(self, parent):
        super(Picker, self).__init__(parent)
        #self._keyPressed = None
        #self.__mouseToBeMoved = True

    def widgetMousePressEvent(self, event):
        super(Picker, self).widgetMousePressEvent(event)
        self.emit(QtCore.SIGNAL("MousePressed(const QMouseEvent&)"), event)

    def widgetMouseReleaseEvent(self, event):
        super(Picker, self).widgetMouseReleaseEvent(event)
        self.emit(QtCore.SIGNAL("MouseReleased(const QMouseEvent&)"), event)

    def widgetMouseDoubleClickEvent(self, event):
        super(Picker, self).widgetMouseDoubleClickEvent(event)
        self.emit(QtCore.SIGNAL("MouseDoubleClicked(const QMouseEvent&)"), event)

    def widgetMouseMoveEvent(self, event):
        #self.__mouseToBeMoved = False
        super(Picker, self).widgetMouseMoveEvent(event)
        self.emit(QtCore.SIGNAL("MouseMoved(const QMouseEvent&)"), event)

    def widgetKeyReleaseEvent(self, event):
        super(Picker, self).widgetKeyReleaseEvent(event)
        if event.key() in [QtCore.Qt.Key_Left,
                          QtCore.Qt.Key_Right,
                          QtCore.Qt.Key_Up,
                          QtCore.Qt.Key_Down]:
            ddict = {}
            ddict['event'] = 'PanningSignal'
            if event.key() == QtCore.Qt.Key_Left:
                ddict['direction'] = 'left'
            elif event.key() == QtCore.Qt.Key_Right:
                ddict['direction'] = 'right'
            elif event.key() == QtCore.Qt.Key_Up:
                ddict['direction'] = 'up'
            elif event.key() == QtCore.Qt.Key_Down:
                ddict['direction'] = 'down'
            self.emit(QtCore.SIGNAL("PanningSignal"), ddict)

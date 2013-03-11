# Import system libraries
from PyEELS.external.qt import QtCore, QtGui

# Local import
from PyEELS.core.application import Application
from PyEELS.frontend.mainwindow import MainWindow

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------

class PyEELSApp(Application):
    def init_qt_elements(self):
        self.app = QtGui.QApplication([])

        #self.widget = self.widget_factory(config=self.config)

        self.window = MainWindow(self.app)
        self.window.init_main_frame()
        self.window.init_status_bar()
        self.window.init_menu_bar()

        self.window.setWindowTitle('PyEELS')

    def init_signal(self):
        pass

    def initialize(self, argv=None):
        self.init_qt_elements()
        self.init_signal()

    def start(self):
        # Draw the window
        self.window.show()
        self.window.raise_()

        # Start the application
        self.app.exec_()

#-----------------------------------------------------------------------------
# Main entry point
#-----------------------------------------------------------------------------

def launch_new_instance():
    """Create and run new PyEELS instance"""
    app = PyEELSApp()
    app.initialize()
    app.start()

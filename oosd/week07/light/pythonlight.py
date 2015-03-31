import sys
from PyQt4 import QtCore, QtGui, uic
import light

qtCreatorFile = "pythonlight.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class LightApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.light = light.Light()
        self.lightDisplay.setText(self.light.show())
        self.lightSwitch.released.connect(self.toggle)

    def toggle(self):
        self.light.switch()
        self.lightDisplay.setText(self.light.show())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = LightApp()
    window.show()
    sys.exit(app.exec_())

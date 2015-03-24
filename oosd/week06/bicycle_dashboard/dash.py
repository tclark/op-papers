import sys
from PyQt4 import QtCore, QtGui, uic
import bicycle
import speedometer
import caloriemeter

qtCreatorFile = "dashboard.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class DashApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.bike = bicycle.Bicycle()
        self.speedometer = speedometer.Speedometer(self.bike)
        self.caloriemeter = caloriemeter.Caloriemeter(self.bike)
        self.rpm_input.editingFinished.connect(self.update_rpms)

    def update_rpms(self):
        new_rpms = int(self.rpm_input.text())
        self.bike.current_rpms = new_rpms
        #self.bike.set_rpms(new_rpms)
        self.kph_display.setText(str(self.speedometer.speed))
        self.calories_display.setText(str(self.caloriemeter.cals))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DashApp()
    window.show()
    sys.exit(app.exec_())

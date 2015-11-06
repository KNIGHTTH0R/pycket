from PyQt4 import QtGui, QtCore  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import mainWindow  # This file holds our MainWindow and all design related things

import captureThread

from PyQt4.QtCore import SIGNAL



class pycketGUI(QtGui.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.startCaptureBtn.clicked.connect(self.start_capture)

        # Variables pour contenir les paquets traites (evite de les stocker sous formes d'objet Qt)
        self.currentPackets = []

        # Counter de nombre de paquets
        self.packetsCounter = 0

        # On set les colonnes de la liste
        listHeaderLabels = QtCore.QStringList()
        listHeaderLabels.append('#')
        listHeaderLabels.append('Time')
        listHeaderLabels.append('Source')
        listHeaderLabels.append('Destination')
        listHeaderLabels.append('Protocol')
        self.packetsList.setHeaderLabels(listHeaderLabels)
        self.packetsList.setSortingEnabled(True)



    def start_capture(self):
        print('Starting capture from GUI')
        self.captureThread = captureThread.Capture()

        # On connect le signale add packet a la fonction locale
        self.connect(self.captureThread, SIGNAL("add_packet(PyQt_PyObject)"), self.add_packet)
        # On connect le signal de la fin du thread avec la fonction locale done
        self.connect(self.captureThread, SIGNAL("finished()"), self.done)
        # Signale qui indique que l'user n'a pas les droits suffisants pour capturer des paquets sur le reseau
        self.connect(self.captureThread, SIGNAL("error_user_privilege(QString)"), self.error_user_privilege)
        # On bind le bouton stop
        self.stopCaptureBtn.clicked.connect(self.captureThread.terminate)

        self.stopCaptureBtn.setEnabled(True)
        self.startCaptureBtn.setEnabled(False)

        # On lance la capture
        self.captureThread.start()


    def error_user_privilege(self, msg):
        QtGui.QMessageBox.information(self, "Error", "Your user doesn't have the priviledges required to capture packets.\
        Please check your permissions. "+msg)


    def done(self):
        self.stopCaptureBtn.setEnabled(False)
        self.startCaptureBtn.setEnabled(True)

    def add_packet(self, packetToAdd):
        packetToAdd.id = self.packetsCounter
        self.currentPackets.append(packetToAdd)
        self.packetsCounter += 1

        item = QtGui.QTreeWidgetItem(self.packetsList)
        item.setText(0, str(packetToAdd.id))
        item.setText(1, str(packetToAdd.created))
        item.setText(2, str(packetToAdd.layers[1]['Source Address']))
        item.setText(3, str(packetToAdd.layers[1]['Destination Address']))
        item.setText(4, str(packetToAdd.layers[2]['LayerType']))




def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    mainWin = pycketGUI()
    mainWin.show()
    app.exec_()


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function

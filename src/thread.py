from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from src.canbus import CanBus

class CanBusThread(QObject):
    dumpSig = pyqtSignal(str, str, str, str, arguments=['time', 'can_id', 'dlc', 'data'])

    def __init__(self, parent=None):
        super(CanBusThread, self).__init__(parent)

        self.__threads = None


    @pyqtSlot()
    def dump(self):
        # CanBus Thread Start
        self.__threads = []
        worker = CanBus()
        thread = QtCore.QThread(self)
        self.__threads.append((thread, worker))
        worker.moveToThread(thread)

        worker.dumpSig.connect(self.dumpSig)
        thread.started.connect(worker.dump)
        thread.start()

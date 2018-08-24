from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from src.canbus import CanBus

class CanBusThread(QObject):
    dumpSig = pyqtSignal(str, str, str, str, arguments=['time', 'can_id', 'dlc', 'data'])
    dumpInit = pyqtSignal()

    def __init__(self, parent=None):
        super(CanBusThread, self).__init__(parent)

        self.__threads = None

    @pyqtSlot()
    def dump(self):
        """ CanBus Thread Start """
        self.dumpInit.emit()

        self.__threads = []
        worker = CanBus()
        thread = QtCore.QThread(self)
        self.__threads.append((thread, worker))
        worker.moveToThread(thread)

        worker.dumpSig.connect(self.dumpSig)
        worker.dumpDone.connect(self.dumpDone)
        thread.started.connect(worker.dump)

        thread.start()

    @pyqtSlot()
    def abortDump(self):
        for thread, worker in self.__threads:
            worker.abort_dump()

    @pyqtSlot()
    def dumpDone(self):
        for thread, worker in self.__threads:
            thread.quit()
            thread.wait()
        print("Dump Thread Finished")

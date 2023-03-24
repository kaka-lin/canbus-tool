from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot

from src.threads.dump_thread import DumpThread
from src.threads.send_thread import SendThread


class CanMainThread(QObject):
    dumpSig = pyqtSignal(str, str, str, str, arguments=['time', 'can_id', 'dlc', 'data'])
    dumpInit = pyqtSignal()

    def __init__(self, parent=None):
        super(CanMainThread, self).__init__(parent)

        self.__thread_maps = {}

    @pyqtSlot()
    def dump(self):
        """ Can Dump Thread Start """
        self.dumpInit.emit()

        worker = DumpThread()
        thread = QtCore.QThread(self)
        self.__thread_maps['dump'] = [thread, worker]
        worker.moveToThread(thread)

        worker.dumpSig.connect(self.dumpSig)
        worker.dumpDone.connect(self.dumpDone)
        thread.started.connect(worker.dump)

        thread.start()

    @pyqtSlot()
    def abortDump(self):
        if 'dump' in self.__thread_maps:
            thread, worker = self.__thread_maps['dump']
            worker.abort_dump()

    @pyqtSlot()
    def dumpDone(self):
        if 'dump' in self.__thread_maps:
            thread, worker = self.__thread_maps['dump']
            thread.quit()
            thread.wait()
        print("Dump Thread Finished")

    @pyqtSlot(str, str, str)
    def send(self, can_id, dlc, data):
        worker = SendThread()
        thread = QtCore.QThread(self)
        self.__thread_maps['send'] = [thread, worker]
        worker.moveToThread(thread)

        worker.sendDone.connect(self.sendDone)
        thread.started.connect(lambda: worker.send(can_id, dlc, data))

        thread.start()

    @pyqtSlot()
    def sendDone(self):
        if 'send' in self.__thread_maps:
            thread, worker = self.__thread_maps['send']
            thread.quit()
            thread.wait()
        print("Send Thread Finished")


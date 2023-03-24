import datetime
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot

from src.app.canbus import CanBus


class DumpThread(QObject):
    dumpSig = pyqtSignal(str, str, str, str, arguments=[
                         'time', 'can_id', 'dlc', 'data'])
    dumpDone = pyqtSignal()

    def __init__(self, parent=None):
        super(DumpThread, self).__init__(parent)

        self.can_bus = CanBus()
        self.__abort = False

    @pyqtSlot()
    def dump(self):
        while True:
            if self.__abort:
                break

            msg = self.can_bus.recv(0.5)
            if msg is not None:
                timestamp = msg.timestamp
                time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
                can_id = hex(msg.arbitration_id)
                dlc = str(msg.dlc).zfill(2)
                data = ' '.join(format(byte, 'x').zfill(2).upper()
                                for byte in msg.data)
                self.dumpSig.emit(time, can_id, dlc, data)

        self.dumpDone.emit()

    @pyqtSlot()
    def abort_dump(self):
        self.__abort = True

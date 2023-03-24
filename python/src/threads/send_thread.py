import datetime
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot

from src.app.canbus import CanBus


class SendThread(QObject):
    sendDone = pyqtSignal()
    sendError = pyqtSignal()

    def __init__(self, parent=None):
        super(SendThread, self).__init__(parent)

        self.can_bus = CanBus()

    @pyqtSlot(str, str, str)
    def send(self, can_id, dlc, hex_string):
        data_len = len(hex_string) // 2
        if data_len != dlc:
            self.sendError.emit()

        # hex string to int
        # -> With the 0x prefix, Python can distinguish hex and decimal automatically
        can_id = int(can_id, 0)
        dlc = int(dlc)
        byte_data = bytes.fromhex(hex_string)
        self.can_bus.transmit(can_id, dlc, byte_data)

        self.sendDone.emit()

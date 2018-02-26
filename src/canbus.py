import datetime
import codecs
import platform
import can
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from PyQt5.QtQml import QJSValue

class CanBus(QObject):
    dumpSig = pyqtSignal(str, str, str, str, arguments=['time', 'can_id', 'dlc', 'data'])

    """ CAN Bus configure"""
    def __init__(self, parent=None):
        super(CanBus, self).__init__(parent)

        if platform.system() == 'Darwin':
            can.util.CONFIG_FILES.extend(
                [
                    'can.ini',
                    '~/.canrc',
                ]
            )

        config = can.util.load_config()
        bitrate = 125000
        tseg1 = 6
        tseg2 = 2
        sjw = 2

        if config['interface'] == None:
            config = {'interface': 'virtual', 'channel': 'test'}
            self._can_bus = can.interface.Bus('test', bustype='virtual')
        elif config['interface'] == 'kvaser':
            self._can_bus = can.interface.Bus(bitrate=bitrate, tseg1=tseg1, tseg2=tseg2, sjw=sjw, **config)
        elif config['interface'] == 'socketcan_native':
            self._can_bus = can.interface.Bus(bitrate=bitrate, **config)
        else:
            self._can_bus = can.interface.Bus(**config)

        print(config)


    def send(self, msg, request=None, timeout=None):
        """ Send CAN message to CAN bus """
        try:
            self._can_bus.send(msg)
        except can.CanError as err:
            print(err)


    def recv(self, timoeout=None):
        """ Receive CAN message from CAN bus """
        return self._can_bus.recv(timoeout)

    @pyqtSlot()
    def shutdown(self):
        """ Shutdown CAN bus """
        self._can_bus.shutdown()

    @pyqtSlot()
    def flush(self):
        print('------------------- flush buffer -------------------')
        self.shutdown()
        self.__init__()
        print('------------------- End!!! -------------------')

    @pyqtSlot()
    def dump(self):
        for msg in self._can_bus:
            timestamp = msg.timestamp
            time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
            can_id = hex(msg.arbitration_id)
            dlc = str(msg.dlc).zfill(2)
            data = ' '.join(format(byte, 'x').zfill(2).upper() for byte in msg.data)
            self.dumpSig.emit(time, can_id, dlc, data)

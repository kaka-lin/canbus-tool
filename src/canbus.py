import codecs
import can
import platform
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from PyQt5.QtQml import QJSValue

class CanBus(QObject):
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

    @pyqtSlot('QJSValue')
    def dump(self, callback):
        msg = self.recv(1.0)
        can_id, data = '', ''

        if msg is None:
            callback.call([QJSValue(can_id), QJSValue(data)])
        else:
            can_id = hex(msg.arbitration_id)
            data = str(codecs.encode(msg.data, 'hex_codec'))

            callback.call([QJSValue(can_id), QJSValue(data)])

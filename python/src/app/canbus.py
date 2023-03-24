import datetime
import codecs
import platform

from PyQt5.QtCore import QObject
import can

# class Singleton(type):
#     """ Singleton metaclass """
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]


# metaclass=Singleton
class CanBus(QObject):
    # Singleton
    _instances = None
    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
        return cls._instances

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
        elif platform.system() == 'Linux':
            can.util.CONFIG_FILES.extend(
                [
                    '~/can.conf',
                    '$HOME/.canrc',
                ]

            )

        config = can.util.load_config()
        bitrate = 125000
        tseg1 = 6
        tseg2 = 2
        sjw = 2

        self.can_type = ''

        if config['interface'] == None:
            config = {'interface': 'virtual', 'channel': 'test'}
            self._can_bus = can.interface.Bus('test', bustype='virtual')
            self.can_type = 'virtual'
        elif config['interface'] == 'kvaser':
            self._can_bus = can.interface.Bus(bitrate=bitrate, tseg1=tseg1, tseg2=tseg2, sjw=sjw, **config)
            self.can_type = 'kvaser'
        elif config['interface'] == 'socketcan_native':
            self._can_bus = can.interface.Bus(**config)
            self.can_type = 'socketcan'
        else:
            self._can_bus = can.interface.Bus(**config)
            self.can_type = config['interface']

    def state(self):
        return self._can_bus.state

    def send(self, msg, request=None, timeout=None):
        """ Send CAN message to CAN bus """
        try:
            self._can_bus.send(msg)
        except can.CanError as err:
            print(err)

    def recv(self, timoeout=None):
        """ Receive CAN message from CAN bus """
        return self._can_bus.recv(timoeout)

    def shutdown(self):
        """ Shutdown CAN bus """
        self._can_bus.shutdown()

    def flush(self):
        print('------------------- flush buffer -------------------')
        self.shutdown()
        self.__init__()
        print('------------------- End!!! -------------------')

    def set_filters(self, filters=None):
        if self.can_type != 'virtual':
            self._can_bus.set_filters(filters)

    ###########################################################################

    def transmit(self, can_id, dlc, data):
        can_msg = can.Message(
            arbitration_id=can_id, dlc=dlc, data=data)
        self.send(can_msg)

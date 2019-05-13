from bikevr_sensor_controller.common.user_descriptor import UserDescriptor
from bikevr_sensor_controller.common.format_descriptor import FormatDescriptor
from bikevr_sensor_controller.common.tools import bit_bool, to_bool
from bluezero import peripheral
from threading import Thread
from time import sleep

NAME = 'Wiimote Status Characteristic'

POLL_RATE = 0.1 #seconds

class WiiStatusCharacteristic(peripheral.Characteristic):    
    def __init__(self, uuid, service, wiimote):
        peripheral.Characteristic.__init__(self,
                                uuid,
                                ['read', 'notify'],
                                service,
                                bit_bool(False))  # starting value
        self.add_descriptor(UserDescriptor(NAME, self))
        self.add_descriptor(FormatDescriptor([0x01, 0x00, 0x00, 0x27, 0x01, 0x00, 0x00], self))

        self.add_notify_event(self.notify_event)
        self.wiimote = wiimote

        self.connected = False
        

    def ReadValue(self, options):
        return self.value

    def notify_event(self):
        if self.notifying:
            self.thread = Thread(target = self.run, args = ())
            self.thread.setDaemon(True)
            self.thread.start()
        else:
            self.thread.join()

    def start_watcher(self):
        self.connected = True
        ping_thread = Thread(target = self.ping, args = ())
        ping_thread.setDaemon(True)
        ping_thread.start()

    def ping(self):
        while self.connected:
            try:
                self.wiimote().request_status()
                self.connected = True
            except RuntimeError:
                self.connected = False
            sleep(POLL_RATE)

    def run(self):
        while self.notifying:
            if (to_bool(self.value) != self.connected):
                self.send_notify_event(bit_bool(self.connected))
                                    
            sleep(POLL_RATE)

from bikevr_sensor_controller.common.user_descriptor import UserDescriptor
from bikevr_sensor_controller.common.format_descriptor import FormatDescriptor
from bikevr_sensor_controller.common.tools import sint16, to_int
from bluezero import peripheral
from threading import Thread
from time import sleep

NAME = 'Name of Characteristic'

POLL_RATE = 0.1 #seconds

class TemplateCharacteristic(peripheral.Characteristic):    
    def __init__(self, uuid, service):
        peripheral.Characteristic.__init__(self,
                                uuid,
                                ['read', 'notify'],
                                service,
                                sint16(0))  # starting value
        self.add_descriptor(UserDescriptor(NAME, self))
        self.add_descriptor(FormatDescriptor([0x0E, 0x00, 0x00, 0x27, 0x01, 0x00, 0x00], self))

        self.add_notify_event(self.notify_event)
        

    def ReadValue(self, options):
        return self.value

    def notify_event(self):
        if self.notifying:
            self.thread = Thread(target = self.run, args = ())
            self.thread.setDaemon(True)
            self.thread.start()
        else:
            self.thread.join()

    def run(self):
        while self.notifying:
            # 1. Get new value
            # 2. Check whether value has changed
            # 3. Use self.send_notify_event to propagrate changes
            
            sleep(POLL_RATE)

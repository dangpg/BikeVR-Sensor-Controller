from bikevr_sensor_controller.common.user_descriptor import UserDescriptor
from bikevr_sensor_controller.common.format_descriptor import FormatDescriptor
from bikevr_sensor_controller.common.tools import sint16, to_int
from bluezero import peripheral
from threading import Thread
from time import sleep
import RPi.GPIO as GPIO

NAME = 'IR Characteristic'

INPUT_PIN1 = 7
INPUT_PIN2 = 22

class IRCharacteristic(peripheral.Characteristic):    
    def __init__(self, uuid, service):
        peripheral.Characteristic.__init__(self,
                                uuid,
                                ['read', 'notify'],
                                service,
                                sint16(0))
        self.add_descriptor(UserDescriptor(NAME, self))
        self.add_descriptor(FormatDescriptor([0x0E, 0x00, 0x00, 0x27, 0x01, 0x00, 0x00], self))

        self.add_notify_event(self.notify_event)

        self.count = 0

        self.prev1 = False
        self.curr1 = False
        self.prev2 = False
        self.curr2 = False

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(INPUT_PIN1, GPIO.IN)
        GPIO.setup(INPUT_PIN2, GPIO.IN)

    def ReadValue(self, options):
        return self.value

    def notify_event(self):
        if self.notifying:
            self.thread = Thread(target = self.run, args = ())
            self.thread.setDaemon(True)
            self.thread.start()
            self.send_notify_event(sint16(self.count))
        else:
            self.thread.join()

    def run(self):
        while self.notifying:
            self.curr1 = GPIO.input(INPUT_PIN1)
            if (not self.curr1 and self.curr1 != self.prev1):
                self.count += 1
                self.send_notify_event(sint16(self.count))
            self.prev1 = self.curr1

            self.curr2 = GPIO.input(INPUT_PIN2)
            if (not self.curr2 and self.curr2 != self.prev2):
                self.count += 1
                self.send_notify_event(sint16(self.count))
            self.prev2 = self.curr2

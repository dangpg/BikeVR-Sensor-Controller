from bikevr_sensor_controller.characteristic.counter_characteristic import CounterCharacteristic
from bikevr_sensor_controller.characteristic.ir_characteristic import IRCharacteristic
from bikevr_sensor_controller.characteristic.wii_status_characteristic import WiiStatusCharacteristic
from bikevr_sensor_controller.characteristic.wii_buttons_characteristic import WiiButtonsCharacteristic
from bikevr_sensor_controller.common.wiimote import Wiimote
from bluezero import peripheral
from threading import Thread
from time import sleep


def run():
    SRVC_UUID = '00000000-0000-4b23-9358-f235b978d07c'
    CHAR_SENSOR_IR_UUID = '11111111-1111-4b23-9358-f235b978d07c'
    CHAR_WII_STATUS_UUID = '22222222-2222-4b23-9358-f235b978d07c'
    CHAR_WII_BUTTONS_UUID = '33333333-3333-4b23-9358-f235b978d07c'
    CHAR_DEBUG_COUNTER_UUID = '99999999-1111-4b23-9358-f235b978d07c'

    wiimote = None

    app = peripheral.Application()

    service = peripheral.Service(SRVC_UUID, True) # Primary service
    service.add_characteristic(IRCharacteristic(CHAR_SENSOR_IR_UUID, service))
    wii_status_char = WiiStatusCharacteristic(CHAR_WII_STATUS_UUID, service, lambda : wiimote)
    service.add_characteristic(wii_status_char)
    service.add_characteristic(WiiButtonsCharacteristic(CHAR_WII_BUTTONS_UUID, service, lambda : wiimote))
    service.add_characteristic(CounterCharacteristic(CHAR_DEBUG_COUNTER_UUID, service))

    app.add_service(service)

    app.start()
"""     
    app_thread = Thread(target = app.start, args = ())
    app_thread.setDaemon(True)
    app_thread.start()

    sleep(1) # wait until app_thread has started

    while app_thread.isAlive():
        cmd = raw_input("> ")
        if cmd == 'exit' or cmd == 'quit':
            break
        elif cmd == 'wii':
            print 'Press 1+2 on your Wiimote now...'
            for i in range(1, 4):
                print 'Attempt ' + str(i)
                try:
                    wiimote = Wiimote()
                    wii_status_char.start_watcher()
                    print 'Wiimote successfully connected!'
                    break
                except RuntimeError:
                    if i == 3:
                        print 'Error trying to establish connection!' 
"""

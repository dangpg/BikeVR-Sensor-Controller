from bluezero import peripheral

class Characteristic(peripheral.Characteristic):
    def __init__(self, uuid, service, readValue):
        peripheral.Characteristic.__init__(self,
                                           uuid,
                                           ['read', 'notify'],
                                           service,
                                           [0x00])
        self.readValue = readValue
        
    def ReadValue(self, options):
        return self.readValue()

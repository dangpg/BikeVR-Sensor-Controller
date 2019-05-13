from bluezero import peripheral
import array

class UserDescriptor(peripheral.Descriptor):
    UUID = '2901'
    def __init__(self, name, characteristic):
        self.value = array.array('B', str.encode(name, 'utf-8')).tolist()
        peripheral.Descriptor.__init__(
            self,
            self.UUID,
            ['read'],
            characteristic)
        
    def ReadValue(self, options):
        return self.value

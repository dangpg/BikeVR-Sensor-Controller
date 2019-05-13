from bluezero import peripheral
import array

class FormatDescriptor(peripheral.Descriptor):
    UUID = '2904'
    def __init__(self, format_value, characteristic):
        self.value = array.array('B', format_value).tolist()
        peripheral.Descriptor.__init__(
            self,
            self.UUID,
            ['read'],
            characteristic)
        
    def ReadValue(self, options):
        return self.value

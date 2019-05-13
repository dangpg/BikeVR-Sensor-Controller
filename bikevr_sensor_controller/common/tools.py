from struct import pack, unpack

def bit_bool(value):
    return pack('?', value)

def to_bool(value):
    return unpack('?', value)[0]

def sint16(value):
    return pack('i', value)

def to_int(value):
    return unpack('i', value)[0]

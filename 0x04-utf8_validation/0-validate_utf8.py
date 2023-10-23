#!/usr/bin/python3
def validUTF8(data):
    byte_count = 0

    for byte in data:
        byte_bin = format(byte, '08b')
        if byte_count == 0:
            if byte_bin[0] == '0':
                continue
            elif byte_bin.startswith('110'):
                byte_count = 1
            elif byte_bin.startswith('1110'):
                byte_count = 2
            elif byte_bin.startswith('11110'):
                byte_count = 3
            else:
                return False
        else:
            if not byte_bin.startswith('10'):
                return False
            byte_count -= 1

    return byte_count == 0

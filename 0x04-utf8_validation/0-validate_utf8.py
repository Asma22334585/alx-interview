#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """check  if data is a valid UTF-8 encoding"""

    num_byte = 0

    for i in range(len(data)):
        if num_byte == 0:
            if data[i] >> 5 == 0b110:
                num_byte = 1
            elif data[i] >> 4 == 0b1110:
                num_byte = 2
            elif data[i] >> 3 == 0b11110:
                num_byte = 3
            elif data[i] >> 7 != 0:
                return False
        else:
            if data[i] >> 6 != 0b10:
                return False
            num_byte -= 1

    return num_byte == 0

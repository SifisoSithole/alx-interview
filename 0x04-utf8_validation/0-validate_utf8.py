#!/usr/bin/python3
"""
validate_utf8
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """

    num_bytes = 0

    # Iterate over each byte in the data
    for byte in data:
        # If this is the start of a new character, determine its length
        if num_bytes == 0:
            if byte >> 7 == 0:
                # This is a single-byte character
                continue
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # This byte should be a continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If there are any unfinished characters, the data is invalid
    return num_bytes == 0

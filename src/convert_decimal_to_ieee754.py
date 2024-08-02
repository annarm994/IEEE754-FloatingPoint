# 1. Convert Decimal to IEEE 754 Format

import struct

def float_to_ieee754(number):
    packed = struct.pack('!f', number)
    binary_str = ''.join(f'{c:08b}' for c in packed)
    return binary_str

print("Decimal to IEEE 754 Format:")
print(float_to_ieee754(0.1))
print()
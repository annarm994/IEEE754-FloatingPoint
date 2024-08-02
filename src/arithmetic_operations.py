# 2. Arithmetic Operations

import struct

def float_to_ieee754(number):
    packed = struct.pack('!f', number)
    binary_str = ''.join(f'{c:08b}' for c in packed)
    return binary_str

result1 = 0.1 + 0.2
result2 = 1.0 / 3.0

ieee_result1 = float_to_ieee754(result1)
ieee_result2 = float_to_ieee754(result2)

print("Arithmetic Operations:")
print(f"0.1 + 0.2 = {result1}, IEEE 754: {ieee_result1}")
print(f"1.0 / 3.0 = {result2}, IEEE 754: {ieee_result2}")

print(f"Expected 0.1 + 0.2: 0.30000000000000004, Actual: {result1}")
print(f"Expected 1.0 / 3.0: 0.3333333333333333, Actual: {result2}")
print()
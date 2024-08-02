# 5. Underflow and Overflow

print("Underflow and Overflow:")

large_number = 1e308
try:
    overflow_result = large_number * 1e10
    print(f"Overflow result: {overflow_result}")
except OverflowError as e:
    print(f"Overflow error: {e}")

small_number = 1e-308
underflow_result = small_number / 1e10
print(f"Underflow result: {underflow_result}")
print()
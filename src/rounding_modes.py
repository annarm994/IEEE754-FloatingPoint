# 4. Rounding Modes

import decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
half_up = decimal.Decimal('1.25').quantize(decimal.Decimal('1.0'))
print("Rounding Modes:")
print(f"ROUND_HALF_UP: {half_up}")

decimal.getcontext().rounding = decimal.ROUND_DOWN
down = decimal.Decimal('1.25').quantize(decimal.Decimal('1.0'))
print(f"ROUND_DOWN: {down}")
print()
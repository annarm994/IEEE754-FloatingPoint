# 6. Visualizing Precision Loss

import numpy as np
import matplotlib.pyplot as plt

small_numbers = np.logspace(-308, -1, num=100)
large_numbers = np.logspace(1, 308, num=100)

small_diff = np.diff(small_numbers)
large_diff = np.diff(large_numbers)

print("Visualizing Precision Loss:")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(small_numbers[:-1], small_diff)
plt.title('Precision Loss in Small Numbers')
plt.xlabel('Number')
plt.ylabel('Difference')

plt.subplot(1, 2, 2)
plt.plot(large_numbers[:-1], large_diff)
plt.title('Precision Loss in Large Numbers')
plt.xlabel('Number')
plt.ylabel('Difference')

plt.tight_layout()
plt.show()
print()

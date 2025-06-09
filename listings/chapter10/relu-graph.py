import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10, 10, 1000)
y = []
for x_i in x:
    y.append(max(0, x_i))

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.plot(x, y, color='red')
plt.show()

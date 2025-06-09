import matplotlib.pyplot as plt
import numpy as np
import math

factor = 0.05 # Nicht zu klein, so dass der Effekt sichtbar ist
x = np.linspace(-10, 10, 1000)
y = []
for x_i in x:
    y.append(factor * x_i if x_i < 0 else x_i)

plt.plot(x, y, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.show()

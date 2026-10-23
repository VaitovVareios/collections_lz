import matplotlib.pyplot as plt 
import numpy as np # I am importing all module

# Creading label for line
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Creading array for X
x1 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# We find y
y1 = np.square(x1)

y2 = np.power(x1, 3)

y3 = np.exp(x1)

y4 = np.log(x1)

# Drawing line for funсtions
plt.plot(x1, y1, color="green", marker="o", markersize=5)
plt.plot(x1, y2, color="blue", marker="*", markersize=5)
plt.plot(x1, y3, color="red", marker="s", markersize=5)
plt.plot(x1, y4, color="yellow", marker="D", markersize=5)
plt.grid(True)
plt.legend()
plt.show()
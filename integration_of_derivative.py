import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from scipy.integrate import simps

# Create array from 0 to 5
x = np.linspace(0, 5, 1000)
y = x ** 2

# Find the derivative of var^2
var = sym.Symbol('var')
print("dervitive is: ", sym.diff(var ** 2))

# Create an array of the derivative
z = 2 * x

# Plot the function, and derivative
plt.plot(x, y)
plt.plot(x, z)
plt.show()

# Find the area under the curve of the derivative from x = 0 to 5
integration = simps(z, x)
print(integration)

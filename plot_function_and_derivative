import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import math
import sympy as sym

x = sym.Symbol('x')

# Get x coordinates
x_list = []
for i in range (-50, 51):
    x_list.append(i)

# Get y coordinates of main function
# Our function is x^2
y_list  = []
for i in range(0, len(x_list)):
    y = x_list[i] ** 2
    y_list.append(y)

#Figure out the derivative of x^2
x = sym.Symbol('x')
print("The derivative of x^2 is: ", sym.diff(x ** 2))

# Get y coordinates for the derivative of 2*x
y_derivative_list = []
for i in range(0, len(x_list)):
    y_deriv_point = 2 * x_list[i]
    y_derivative_list.append(y_deriv_point)

# Create dataframe
df = pd.DataFrame.from_dict({'x': x_list, 'y_function': y_list, 'deriv_function' : y_derivative_list})

#Plot the 2 functions, both the function and the derivative
df.plot(x='x', y='y_function')
df.plot(x='x', y = 'deriv_function')
plt.show()

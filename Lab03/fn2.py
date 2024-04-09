import numpy as np
import matplotlib.pyplot as plt
from math import cos

# Initialize variables
xn = 0.5
tol1 = 0.05
ea = tol1 + 1
xnVal = np.array([[0, xn, np.nan, np.nan]])
k = 0

# Convergence calculation
while ea > tol1:
    xn1 = cos(xn)
    Ea = abs(xn1 - xn)
    ea = abs((xn1 - xn) / xn) * 100
    k += 1
    xnVal = np.vstack([xnVal, [k, xn1, Ea, ea]])
    xn = xn1

# Plotting the approximate error with iterations
plt.figure()
plt.plot(xnVal[1:, 2], '*-b')
plt.xlabel('iterations (n)')
plt.ylabel('Ea')
plt.title('Approximate error with iterations')
plt.grid(True)
plt.show()

# Plotting the approximate error: En+1 vs En
plt.figure()
plt.plot(xnVal[:-1, 2], xnVal[1:, 2], '*-b')
plt.xlabel('Ea_n')
plt.ylabel('Ea_n+1')
plt.title('Approximate error: En+1 vs En')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from math import exp, log

# Initialize variables
xn = 5
Ea = 1
tol1 = 10**-8
xnA = []

# Newton-Raphson method
while Ea > tol1:
    xn1 = xn - (exp(-xn) - xn) / (-exp(-xn) - 1)
    Ea = abs(xn1 - xn)
    xnA.append([xn1, Ea])
    xn = xn1

# Convert to numpy array for easier slicing
xnA = np.array(xnA)

# Plotting the approximate absolute error with iterations
plt.figure()
plt.plot(xnA[:, 1], '*-b')
plt.xlabel('iterations (n)')
plt.ylabel('En')
plt.title('Approx absolute error with iterations')
plt.grid(True)
plt.show()

# Plotting the approximate absolute error: En+1 vs En
plt.figure()
plt.plot(xnA[:-1, 1], xnA[1:, 1], '*-b')
plt.xlabel('En')
plt.ylabel('En+1')
plt.title('Approx absolute error: En+1 vs En')
plt.grid(True)
plt.show()

# Plotting the approximate absolute error on a log scale
En = xnA[:-1, 1]
En1 = xnA[1:, 1]
plt.figure()
plt.plot(np.log(En), np.log(En1), '*-b')
plt.xlabel('log(En)')
plt.ylabel('log(En+1)')
plt.title('N-R method: Approximate absolute error on log scale')
plt.grid(True)
plt.show()

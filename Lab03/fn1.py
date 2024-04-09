import numpy as np
import matplotlib.pyplot as plt
from math import cos

# Initialize variables
xn = 0.5
tol1 = 0.0005
xnVal = np.array([[0, xn]])
points = np.array([]).reshape(0,2)

# Iterative process
for k in np.arange(1, 11, 0.1):
    xn1 = cos(xn)
    xnVal = np.vstack([xnVal, [k, xn1]])
    points = np.vstack([points, [xn, xn1], [xn1, xn1]])
    xn = xn1

# Plotting xnVal
plt.plot(xnVal[:,0], xnVal[:,1], '*-b')
plt.xlabel('iterations (n)')
plt.ylabel('xn')

# Define functions
x = np.arange(0, 1.2, 0.001)
gx = np.cos(x)
g1x = -np.sin(x)

# Plotting functions
h = plt.plot(x, gx, 'r', x, x, 'k', points[:,0], points[:,1], '-o', linewidth=2)
plt.legend(['f1(x)=g(x)=cos(x)', 'f2(x)=x'])
plt.xlabel('x')
plt.ylabel('f1(x), f2(x)')
plt.title('x = cos(x) solution')
plt.grid(True)
plt.show()

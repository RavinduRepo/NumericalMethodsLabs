import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos

# Initialize variables
tol1 = 0.00005
xl = 3.7
xu = 4.0
xr = (xl + xu) / 2
results = []

# Calculate initial function values
fxl = sin(10 * xl) + cos(3 * xl)
fxu = sin(10 * xu) + cos(3 * xu)
fxr = sin(10 * xr) + cos(3 * xr)
E = abs(xu - xl) / 2
results.append([xl, xu, xr, E])

itCount = 0

# Bisection method
while E > tol1:
    if fxl * fxr == 0:
        E = 0
    elif fxl * fxr > 0:
        xl = xr
        fxl = fxr
    else:
        xu = xr
        fxu = fxr

    xr = (xl + xu) / 2
    fxr = sin(10 * xr) + cos(3 * xr)
    E = abs(xu - xl) / 2
    results.append([xl, xu, xr, E])
    itCount += 1

print(f"iteration count:{itCount}")

# Convert results to a NumPy array for easier slicing
results = np.array(results)
En = results[:-1, 3]
En1 = results[1:, 3]

# Plotting En vs En+1
plt.plot(En, En1, '-*')
plt.xlabel('En')
plt.ylabel('En+1')
plt.title('Bisection method: Approximate absolute error En+1 vs En')
plt.grid(True)
plt.show()

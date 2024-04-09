import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.01) # making x cordinates from 0 to 5, 0.01 steps 
y = np.sin(10*x) + np.cos(3*x) # function

f1x = np.sin(10*x)
f2x = - np.cos(3*x)

plt.figure()
# plotting
plt.plot(x, y)
plt.grid(True)
plt.show()

plt.figure()
# plotting
plt.plot(x, f1x, label = 'sin(x)')
plt.plot(x, f2x, label = 'cos(x)')
plt.grid(True)
plt.show()


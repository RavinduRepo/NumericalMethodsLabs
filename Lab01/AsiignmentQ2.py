import numpy as np
import matplotlib.pyplot as plt

m = 68.1
c = 12.5
g = 9.8
v0 = 0
dt = 0.2

# Analytical solution
def Analytical(m, c, g, v0, t):
    return (m * g / c) - (m / c) * (g - (m / c) * v0) * np.exp(-c * t / m)

# Generate time values
t = np.arange(0, 32, dt)

# Calculate analytical solution for each time value
analit = [Analytical(m, c, g, v0, time) for time in t]

# Convert list to numpy array
analit = np.array(analit)



# Numerical solutions
v1 = 0
numeric = []
def Numerical(m, c, g, v1, dt):
    return (g - c/m*v1) * dt + v1

for i in t:
    numeric.append(v1)
    v1 = Numerical(m, c, g, v1, dt)




# Plotting
plt.figure()
PA = plt.plot(t, analit, '-k', label='Analytical')  # Analytical solution
PN = plt.plot(t, numeric, '-r', label='Numerical')   # Numerical solution
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

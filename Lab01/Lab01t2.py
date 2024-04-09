import numpy as np
import matplotlib.pyplot as plt

m = 68.1
c = 12.5
g = 9.8
v0 = 0

# Analytical solution
t = np.arange(0, 33, 1)
v = m*g/c - (m/c)*(g - c*v0/m)*np.exp(-c*t/m)
plt.plot(t, v, 'k')

# Numerical solution
delt = 2  # time step
v1 = 0
t1 = 0
TV = np.array([[t1, v1]])

while t1 < 32:
    v2 = (g - c/m*v1)*delt + v1
    t2 = t1 + delt
    TV = np.vstack([TV, [t2, v2]])
    v1 = v2
    t1 = t2

# Plot Both
plt.plot(t, v, 'k')
plt.plot(TV[:, 0], TV[:, 1], '.-m', markersize=15)
plt.show()

# Plot Error
plt.figure()
plt.plot(v - TV[:, 1], '.r')
plt.show()

# Absolute and percentage errors
Output1 = np.column_stack([t, v, TV[:, 1]])
print('       t,       Va,         Vn,       Et,       Epst,     Ea,     Epsa')
Output2 = np.column_stack([Output1, np.abs(Output1[:, 1] - Output1[:, 2]),
                           np.insert(np.abs(Output1[1:, 2] - Output1[:-1, 2]), 0, np.nan),
                           np.abs(Output1[:, 1] - Output1[:, 2]) / Output1[:, 1] * 100,
                           np.insert(np.abs(Output1[1:, 2] - Output1[:-1, 2]) / Output1[1:, 2] * 100, 0, np.nan)])
print(Output2)

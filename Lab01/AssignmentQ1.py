import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
# Define the function and its derivative
def f(x):
    return -0.1*x**4 - 0.5*x**2 - 0.5*x + 1.2
def f_prime(x):
    return -0.4*x**3 - x - 0.5

# Initial values
xi = 0.5
f1xi = f_prime(xi)

# Different step sizes
h_values = np.array([1, 1/2, 1/2**2, 1/2**3, 1/2**4, 1/2**5, 1/2**6, 1/2**7, 1/2**8, 1/2**9, 1/2**10])

# Initialize result arrays
res = []

etF = []
etB = []
etC = []
F = []
B = []
C = []

# Calculate derivatives and errors for each step size
for h in h_values:
    xip1 = xi + h
    xim1 = xi - h

    fxip1 = f(xip1)
    fxim1 = f(xim1)

    dxF = (fxip1 - f(xi)) / h  # forward
    dxB = (f(xi) - fxim1) / h  # backward
    dxC = (fxip1 - fxim1) / (2 * h)  # centered

    et = [f1xi - dxF, f1xi - dxB, f1xi - dxC]  # true error
    res.append([h, f1xi, dxF, dxB, dxC, np.abs(et)])

    F.append(dxF)
    B.append(dxB)
    C.append(dxC)
    etF.append(et[0])
    etB.append(et[1])
    etC.append(et[2])

# Convert results to numpy arrays
res = np.array(res, dtype=object)
etF = np.array(etF)
etB = np.array(etB)
etC = np.array(etC)
F = np.array(F)
B = np.array(B)
C = np.array(C)

#draw the table

print("Step size(h)\t\tf'(0.5)\t\tAbsolute error(e)")
abs_etF = [abs(x) for x in etF]
abs_etB = [abs(x) for x in etB]
abs_etC = [abs(x) for x in etC]
for i in range(len(F)):
    print("%.10f\t\t%.10f\t\t%.10f" %(h_values[i], C[i], abs_etC[i]))



# head = ["Step size(h)", "f'(0.5)", "Absolute error(e)"]
# #Forward
# abs_etF = [abs(x) for x in etF]
# data = [[f"{h:.10f}", f"{df:.10f}", f"{er:.10e}"] for h, df, er in zip(h_values, F, abs_etF)]
# # display table
# print(tabulate(data, headers=head, tablefmt="grid"))

# # Backward
# abs_etB = [abs(x) for x in etB]
# data = [[f"{h:.10f}", f"{df:.10f}", f"{er:.10e}"] for h, df, er in zip(h_values, B, abs_etB)]
# # display table
# print(tabulate(data, headers=head, tablefmt="grid"))

# # Centered
# abs_etC = [abs(x) for x in etC]
# data = [[f"{h:.10f}", f"{df:.10f}", f"{er:.10e}"] for h, df, er in zip(h_values, C, abs_etC)]
# # display table
# print(tabulate(data, headers=head, tablefmt="grid"))

# Plot truncation error vs step size
plt.figure()
P1, = plt.plot(h_values, abs_etF, '-ob', label='Forward')  # Forward
P2, = plt.plot(h_values, abs_etB, '-ok', label='Backward')  # Backward
P3, = plt.plot(h_values, abs_etC, '-*r', label='Centered')  # Centered
plt.xlabel('Step size(H)')
plt.ylabel('Absolute error(et)')
plt.legend()
plt.grid(True)

# Plot log-log graph
plt.figure()
P1L, = plt.plot(np.log(h_values), np.log(abs_etF), '--ob', label='Forward')  # Forward
P2L, = plt.plot(np.log(h_values), np.log(abs_etB), '--ok', label='Backward')  # Backward
P3L, = plt.plot(np.log(h_values), np.log(abs_etC), '--*r', label='Centered')  # Centered
plt.xlabel('log(Step size(h))')
plt.ylabel('log(Absolute error)')
plt.legend()
plt.grid(True)
plt.show()

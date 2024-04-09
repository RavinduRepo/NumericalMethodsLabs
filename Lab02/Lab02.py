import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Define the function and its derivative
def f(x):
    return -0.1*x**4 - 0.5*x**2 - 0.5*x + 1.2
def f_prime(x):
    return -0.4*x**3 - x - 0.5

def fDerivative(x, h):
    fdx = (f(x + h) - f(x)) / h
    return fdx

def cDerivative(x, h):
    cdx = (f(x + h) - f(x - h)) / 2 * h
    return cdx

def bDerivative(x, h):
    bdx = (f(x) - f(x - h)) / h
    return bdx


h = 1
xi = 0.5

h_list = []
xip = []
xim = []

fx = []
cx = []
bx = []

fe = []
ce = []
be = []

actual = f_prime(xi)
y = h
while h > y/(10**10):
    
    h_list.append(h)
    xip.append(xi + h)
    xim.append(xi - h)
    fd = fDerivative(xi, h)
    cd = cDerivative(xi, h)
    bd = bDerivative(xi, h)

    fx.append(fd)
    cx.append(cd)
    bx.append(bd)
    fe.append(abs(fd - actual))
    ce.append(abs(cd - actual))
    be.append(abs(bd - actual))

    h = h * 0.1

h_list = np.array(h_list)
xip = np.array(xip)
xim = np.array(xim)

fx = np.array(fx)
cx = np.array(cx)
bx = np.array(bx)

fe = np.array(fe)
ce = np.array(ce)
be = np.array(be)


i = 0
for j in (fe):
    print("forward: %.10f\tcentered: %.10f\tbackward: %.10f" %(fe[i], ce[i], be[i]))
    i+=1

#draw the table
head = ["Step size(h)", "xi+1", "xi-1", "f1(xi)", "Absolute error(F)", "Precentage error(F)", "Absolute error(C)", "Precentage error(C)", "Absolute error(B)", "Precentage error(B)"]
#Forward
data = [[f"{hh:.10f}",f"{xp:.10e}", f"{xm:.10e}", f"{df:.10f}", f"{erf:.10e}", f"{erfp:.10e}", f"{erc:.10e}", f"{ercp:.10e}", f"{erb:.10e}", f"{erbp:.10e}"] for hh, xp, xm, df, erf, erfp, erc, ercp , erb, erbp  in zip(h_list, xip, xim, fx, fe, (fe/fd)*100, ce, (ce/fd)*100, be, (be/fd)*100)]
# display table
print(tabulate(data, headers=head, tablefmt="grid"))

# Plot truncation error vs step size
plt.figure()
P1 = plt.plot(h_list, fe, '-b', label='Forward')  # Forward
P2 = plt.plot(h_list, be, '-k', label='Backward')  # Backward
P3 = plt.plot(h_list, ce, '-r', label='Centered')  # Centered
plt.xlabel('Step size(H)')
plt.ylabel('Absolute error(et)')
plt.legend()
plt.grid(True)

# Plot log-log graph
plt.figure()
P1L = plt.plot(np.log(h_list), np.log(fe), '--b', label='Forward')  # Forward
P2L = plt.plot(np.log(h_list), np.log(be), '--k', label='Backward')  # Backward
P3L = plt.plot(np.log(h_list), np.log(ce), '--r', label='Centered')  # Centered
plt.xlabel('log(Step size(h))')
plt.ylabel('log(Absolute error)')
plt.legend()
plt.grid(True)
plt.show()
#import numpy as np
x = 0.5
y = -0.1*x**4 - 0.5*x**2 - 0.5*x + 1.2
dt = 0.5 #0.25 #0.125

def func(x):
    return (-0.1*x**4 - 0.5*x**2 - 0.5*x + 1.2)

print(y)

#forward
dyf = (func(x+dt) - func(x))/dt
print("Forward: ",dyf)

#backword
dyb = (func(x) - func(x-dt))/dt
print("backword: ",dyb)

#centered
dyc = (func(x + dt) - func(x-dt))/(2*dt)
print("centered: ",dyc)
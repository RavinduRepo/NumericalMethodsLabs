import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import math
# Approch 1
x = 5
terms = 20
ap1 = []
ap1Ans = 0

termNum = [i for i in range(terms)]
for i in termNum:
    ap1Ans += ((-1)**i) * (x**i)/math.factorial(i)
    ap1.append(ap1Ans)



import numpy as np
import matplotlib.pyplot as plt

allowed = 0.0005
for i in np.arange(0, 1, 0.001):
    #print (f"{i}\n")
    if abs(np.cos(i) - i) < allowed:
        print (f"x = {i}\n")
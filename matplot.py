#%%
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x)*np.cos(x))       # Plot the sine of each x point
plt.plot(x,np.abs(1/x*np.pi))
plt.show() 
import numpy as np
import matplotlib.pyplot as plt


plt.style.use('_mpl-gallery')
arr = np.loadtxt("Test_Projects/trainClass1.dat",converters=float)

print(arr)

x_axis_data = 400
y_axis_data = len(arr)

plt.scatter(x_axis_data, y_axis_data, s=None, c=None, marker=None, cmap=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None) 

plt.show()

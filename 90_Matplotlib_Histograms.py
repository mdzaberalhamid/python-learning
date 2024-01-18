import matplotlib.pyplot as plt
import numpy as np

#Matplotlib Histograms

#Creating Histogram

x = np.random.normal(170, 10, 250)
#print(x)

plt.hist(x)

plt.show()

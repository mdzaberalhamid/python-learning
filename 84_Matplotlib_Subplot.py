import matplotlib.pyplot as plt
import numpy as np

#Matplotlib Subplot

#Displaying Multiple Plots

#Plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,5,9])

#plt.subplot(1,2,1)
plt.subplot(2,1,1)
plt.plot(x,y)
#Title
plt.title("SALES")

plt.show()

#Plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,25,40])

#plt.subplot(1,2,2)
plt.subplot(2,1,2)
plt.plot(x,y)
#Title
plt.title("INCOME")

#Main title
plt.suptitle("MY SHOP")

plt.show()

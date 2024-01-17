import matplotlib.pyplot as plt
import numpy as np

#Matplotlib Bars

#Creating Bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
#plt.barh(x,y)                        #Horizontal Bars
#plt.bar(x, y, color='red')       #Bars Color
#plt.bar(x, y, width = 0.1)     #Bars Width
#plt.barh(x, y, height = 0.1)  #Bars Width in Horizontal

plt.show()

import matplotlib.pyplot as plt
import numpy as np

#Matplotlib Pie Charts

#Creating Pie Charts
x = np.array([35, 25, 25, 15])

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
e = [0.2, 0, 0, 0]
mycolors = ["red", "hotpink", "b", "#4CAF50"]

#plt.pie(x)
#plt.pie(x, labels = mylabels)   #Adding labels
#plt.pie(x, labels = mylabels, startangle = 90)  #Starting angle
#plt.pie(x, labels = mylabels, explode = e)        #Explode
#plt.pie(x, labels = mylabels, explode = e, shadow = True)   #Shadow
plt.pie(x, labels = mylabels, colors = mycolors)    #Colors

#plt.legend()    #Legend
plt.legend(title = 'Four Fruits')   #Legend with title

plt.show()

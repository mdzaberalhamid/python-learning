import matplotlib.pyplot as plt
import numpy as np

#Matplotlib Line

#Linestyle
ypoints = np.array([3,8,1,10])

plt.plot(ypoints, linestyle='dashed')
plt.show()

#Shorter Syntax
#plt.plot(ypoints, ls = ':')
#plt.show()

#Line Color
#plt.plot(ypoints, ls = '--', color = 'r')
#plt.show()

#Line Width
#plt.plot(ypoints, ls = '--', color = 'r', linewidth = '10')
#plt.show()

#Multiple Lines
#ypoints2 = np.array([6, 2, 7, 9])

#plt.plot(ypoints, color = 'r', linewidth = '5')
#plt.plot(ypoints2, color = 'g', linewidth = '5', linestyle = '--')

#plt.show()

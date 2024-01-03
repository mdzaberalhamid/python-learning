print('Python Matplotlib Markers')

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

#Markers

#plt.plot(ypoints, marker = 's')
#plt.show()

# Format Strings

#plt.plot(ypoints, 'o:r')
#plt.plot(ypoints, 'o-g')
#plt.plot(ypoints, 'o--b')
#plt.show()

#Marker Size, Color, Face Color

#plt.plot(ypoints, marker = 'o', ms = 10)
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'g', mfc = 'r')
plt.show()

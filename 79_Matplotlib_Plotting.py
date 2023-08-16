print("Matplotlib Plotting")

print("\nPlotting With Line")
print("Example:")
print("Draw a line in a diagram from position (1, 3) to position (8, 10):")

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints)
plt.show()


print("\nPlotting Without Line")
print("Example")
print("Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):")

xps1 = np.array([1,8])
yps1 = np.array([3,10])

plt.plot(xps1, yps1, "o")
plt.show()

print("\nMultiple Points")
print("Example")
print("Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):")

xpointsn = np.array([1,2,6,8])
ypointsn = np.array([3,8,1,10])

plt.plot(xpointsn, ypointsn)
plt.show()

print("\nDefault X-Points")
print("Example")
print("Plotting without x-points:")

yn1 = np.array([3, 8, 1, 10, 5, 7])

plt.plot(yn1)
plt.show()

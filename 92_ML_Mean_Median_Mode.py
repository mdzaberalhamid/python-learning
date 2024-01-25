import numpy

#Mean Median Mode

#Calculating Mean
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
print('Mean is: ', x)

#Calculating Median

y = numpy.median(speed)
print('Median is: ', y)

#Calculating Mode
from scipy import stats

z = stats.mode(speed)
print(z)

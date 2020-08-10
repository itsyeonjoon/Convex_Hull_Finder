import matplotlib.pyplot as plt
import numpy as np
from ConvexHull import ConvexHull
import ast

# test
listPoints = [[3, 2], [4, 0], [0, -2], [1, 0], [-1, 1], [1, -1], [-1, 0], [-2, 0], [4, -1], [-2, 4], [3, 0], [1, 5], [0, 0], [2, 3]]

ch = ConvexHull(listPoints)
ch.sort()
result = ch.findConvexHull()
firstPoint = result[0]
result.append(firstPoint)

xAxis = []
yAxis = []
for i in range(0, len(ch.points)): 
    xAxis.append(ch.points[i][0])
    yAxis.append(ch.points[i][1])
plt.plot(xAxis, yAxis, 'bo')

xAxis2 = []
yAxis2 = []
for i in range(0, len(result)): 
    xAxis2.append(result[i][0])
    yAxis2.append(result[i][1])
plt.plot(xAxis2, yAxis2, 'k')

plt.show()


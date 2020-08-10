import matplotlib.pyplot as plt
from ConvexHull import ConvexHull

# test
listPoints = [[3, 2], [4, 0], [0, -2], [1, 0], [-1, 1], [1, -1], [-1, 0], [-2, 0], [4, -1], [-2, 4], [3, 0], [1, 5], [0, 0], [2, 3]]

ch = ConvexHull(listPoints)
ch.sort()
result = ch.findConvexHull()
firstPoint = result[0]
result.append(firstPoint)

xAxis = []
yAxis = []
for i in range(0, len(result)): 
    xAxis.append(result[i][0])
    yAxis.append(result[i][1])
plt.plot(xAxis, yAxis, 'k', xAxis, yAxis, 'bo')

xAxis.clear()
yAxis.clear()

for i in range(0, len(ch.inner)): 
    xAxis.append(ch.inner[i][0])
    yAxis.append(ch.inner[i][1])
plt.plot(xAxis, yAxis, 'ro')

plt.show()


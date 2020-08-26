import matplotlib.pyplot as plt
import ast
from ConvexHull import ConvexHull

# The following code is a Convex Hull Visualizer using matplotlib.pyplot library. 
# It iwll receive the points in a form of 2D list, then display the convex hull and its shape. 
# while all different combination of points will work, try the one I made as a starting point:
# [[10, 2], [4, 9], [3, 2], [5, 1], [-3, 5], [0, -2], [1, 2], [8, 4], [-1, 1], [5, 5], [1, -1], [-1, 0], [-2, 0], [4, -1], [-2, 4], [3, 0], [1, 5], [0, 0], [2, 3]]

# I will soon try to make the visualizer with better user interaction using GUI in the future :) 

listString = input("Please enter the 2D list of points\nin a form such as the following: ex. [[1, 2], [0, 0], [3, 3], ...]\n")
listPoints = ast.literal_eval(listString)
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


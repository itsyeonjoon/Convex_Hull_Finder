"""
Name: Yeon Joon Jung
Date: August 2020
Project: Convex Hull Finder

The ConvexHall class finds the convex hull from the given set of points in Euclidean space
using the Graham Scan Algorithm developed by Ronald Graham in 1972.
"""
from collections import deque 
import math

class ConvexHull: 
    pointAddress = [] # saves address of each points
    minimumY = 0 # saves address of a point that has minimum Y value 

    # __init__ creates a ConvexHull object, initializing the 2D list of 
    # points, pointAddress list, and finds the point with the minimum y value
    # from the given list of points. 
    def __init__(self, points): 
        if len(points) < 3:
            raise ValueError("There should be at least 3 points to form a shape.") 

        self.points = points # list of lists of points
        # self.minimumY = 0 # saves address of a point that has minimum Y value 
        # self.pointAddress = [] # saves address of each points

        self.pointAddress.append(0)
        for i in range (1, len(points)): 
            if points[i][1] < points[self.minimumY][1]: 
                self.minimumY = i
            elif points[i][1] == points[self.minimumY][1]: 
                if points[i][0] < points[self.minimumY][0]:
                    self.minimumY = i
            self.pointAddress.append(i)
        self.pointAddress.remove(self.minimumY) # removes the address of the point with minimum y
    
    # sort() method sorts the pointAddress by its position from the minimumY points.
    # in Graham Scan Algorithm, points must be sorted by the points' and minimumY's polar coordinate angle,
    # starting from the smallest angle. Since we will use stack in the actual algorithm, here we will sort
    # it from greatest to smallest.
    def sort(self): 
        groupLeft = []
        groupRight = []
        for i in range(0, len(self.pointAddress)): 
            if (self.points[self.pointAddress[i]][0] >= self.points[self.minimumY][0]):
                groupRight.append(self.pointAddress[i])
            else:
                groupLeft.append(self.pointAddress[i])
        self.pointAddress.clear()
        self.sortByArctan(groupLeft)
        self.sortByArctan(groupRight)
        self.pointAddress.extend(groupLeft)
        self.pointAddress.extend(groupRight)

    # sorByArctan() method is a helper method for sort(). Here we do the actual sorting of 
    # pointAddress by its angle. I used the arctan value between two points to calculate the angle.
    def sortByArctan(self, group): 
        arctanValue = [] 
        for i in range(0, len(group)): 
            y = self.points[group[i]][1] - self.points[self.minimumY][1]
            x = self.points[group[i]][0] - self.points[self.minimumY][0]
            y = y * 1.0
            try: 
                arctanValue.append(math.atan2(y, x))
            except ZeroDivisionError: 
                arctanValue.append(9999999.99)
        # sort by insertion sort 
        for i in range(0, len(group)): 
            for j in range(i, 0, -1): 
                if arctanValue[j] > arctanValue[j - 1]:
                    group[j - 1], group[j] = group[j], group[j - 1]
                    arctanValue[j - 1], arctanValue[j] = arctanValue[j], arctanValue[j - 1]
    
    # findConvexHull() method computes and finds outer points that forms a smallest convex polygon
    # using Graham Scan Algorithm, from already sorted points in sort() method.
    def findConvexHull(self): 
        hullStack = deque()
        hull = deque()
        inner = deque()

        for i in range(0, len(self.pointAddress)):
            hullStack.append(self.pointAddress[i])
        hull.append(self.minimumY)

        hullCount = 1
        totalCount = len(self.pointAddress)

        while totalCount > 1:
            pt1 = hull[-1] # peek()
            pt2 = hullStack.pop()
            pt3 = hullStack[-1] # peek()

            if self.isCCW(self.points[pt1], self.points[pt2], self.points[pt3]): 
                hull.append(pt2)
                hullCount += 1
                totalCount -= 1
            else: 
                inner.append(pt2)
                hullStack.append(hull.pop())
                hullCount -= 1
                
        pt1 = hull[-1]
        pt2 = hullStack[-1]
        pt3 = self.minimumY
        if self.isCCW(self.points[pt1], self.points[pt2], self.points[pt3]): 
            hull.append(hullStack.pop())
            hullCount += 1

        answer = []
        while hull: 
            answer.append(self.points[hull.pop()])
        return answer  

    # isCCW() returns a boolean whether or not the three points are having a "Left Turn", or having a counter-
    # clockwise turn, or not. It will return true if the points are having a CCW turn, and returns false if they
    # are co-linear or having a clockwise turn. It uses cross product to calculate this.
    def isCCW(self, p1, p2, p3):
        crossProduct = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        if crossProduct > 0:
            return True
        else:
            return False

# test / debugging!!!
# testPoints = [[3, 2], [4, 0], [0, -2], [1, 0], [-1, 1], [1, -1], [-1, 0], [-2, 0], [4, -1], [-2, 4], [3, 0], [1, 5], [0, 0], [2, 3]]
# test1 = ConvexHull(testPoints)
# test1.sort()
# a = test1.findConvexHull()
# print(*a, sep = ", ")
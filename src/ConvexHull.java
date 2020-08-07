// Name: Yeon Joon Jung
// Date: August 2020
// Project: Convex Hull Finder
//
// The ConvexHall class finds the convex hull from the given set of points in Euclidean space
// using the Graham Scan Algorithm developed by Ronald Graham in 1972.

import java.util.*;

public class ConvexHull {
    private int[][] points; // 2D array from the constructor's parameter
    private List<Integer> pointAddress; // ArrayList of Integer saving address to each point in int[][] points
    private int minimumY; // point in the most "down-left" corner within the given set of points

    // Constructor ConvexHull(int[][] points) creates a ConvexHull object, initializing 2D array of points,
    // pointAddress Arraylist, and finds the minimumY of the given set of points.
    // precondition: parameter int[][] points must have at least 3 points.
    //       Exception: throws IllegalArgumentException() if int[][] points's length is less than 3.
    // postcondition: creates a ConvexHull object.
    public ConvexHull(int[][] points) {
        if (points.length < 3) {
            throw new IllegalArgumentException();
        }
        this.points = points;
        pointAddress = new ArrayList<>();
        minimumY = 0;
        pointAddress.add(0);
        for (int i = 1; i < points.length; i++) {
            if (points[i][1] < points[minimumY][1]) {
                minimumY = i;
            } else if (points[i][1] == points[minimumY][1]) {
                if (points[i][0] < points[minimumY][0]) {
                    minimumY = i;
                }
            }
            pointAddress.add(i);
        }
        pointAddress.remove(minimumY);
    }

    // sorts in a reversed way, so that stack entered will be in correct way
    // sort() method sorts the ArrayList pointAddress by its position from the minimumY points.
    // in Graham Scan Algorithm, points must be sorted by the points' and minimumY's polar coordinate angle,
    // starting from the smallest angle. Since we will use stack in the actual algorithm, here we will sort
    // it from greatest to smallest.
    // precondition: N/A
    // postcondition: Sorts the pointAddress in reverse order via polar coordinate angle from minimumY.
    public void sort() {
        List<Integer> groupLeft = new ArrayList<>();
        List<Integer> groupRight = new ArrayList<>();
        for (int i = 0; i < pointAddress.size(); i++) {
            if (points[pointAddress.get(i)][0] >= points[minimumY][0]) {
                groupRight.add(pointAddress.get(i));
            } else {
                groupLeft.add(pointAddress.get(i));
            }
        }
        pointAddress.clear();
        sortByArctan(groupLeft);
        sortByArctan(groupRight);
        pointAddress.addAll(groupLeft);
        pointAddress.addAll(groupRight);
    }

    // findConvexHull() method computes and finds outer points that forms a smallest convex polygon
    // using Graham Scan Algorithm, from already sorted points in sort() method.
    // precondition: N/A
    // postcondition: returns a 2D array composed of points that forms convex hull.
    public int[][] findConvexHull() {
        Stack<Integer> hullStack = new Stack<>();
        for (int i = 0; i < pointAddress.size(); i++) {
            hullStack.push(pointAddress.get(i));
        }

        Stack<Integer> hull = new Stack<>();
        Stack<Integer> inner = new Stack<>();
        hull.push(minimumY);

        int hullCount = 1;
        int totalCount = pointAddress.size(); // totalCount tracks how many elements in the hullStack.

        while (totalCount > 1) {
            int pt1 = hull.peek();
            int pt2 = hullStack.pop();
            int pt3 = hullStack.peek();
            if (isCCW(points[pt1], points[pt2], points[pt3])) {
                hull.push(pt2);
                hullCount++;
                totalCount--;
            } else {
                inner.push(pt2);
                hullStack.push(hull.pop());
                hullCount--;
            }
        }
        hull.push(hullStack.pop());
        hullCount++;

        int[][] answer = new int[hullCount][2];
        int num = 0;
        while (!hull.isEmpty()) {
            answer[num] = points[hull.pop()];
            num++;
        }
        return answer;
    }

    // isCCW() method returns a boolean whether or not the three points are having a "Left Turn", or having a counter-
    // clockwise turn, or not. It will return true if the points are having a CCW turn, and returns false if they
    // are co-linear or having a clockwise turn. It uses cross product to calculate this.
    // precondition: N/A
    // postcondition: returns true if CCW, false otherwise.
    public boolean isCCW(int[] p1, int[] p2, int[] p3) {
        int crossProduct = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]);
        if (crossProduct > 0) {
            return true;
        } else {
            return false;
        }
    }

    // sorByArctan() method is a helper method for sort(). Here we do the actual sorting of pointAddress by its angle.
    // I used the arctan value between two points to calculate the angle.
    // precondition: N/A
    // postcondition: Sorts the group in reverse order via polar coordinate angle from minimumY.
    // I used insertion sort here. It could be changed to Mergesort or Quicksort in the future for faster computation.
    private void sortByArctan(List<Integer> group) {
        double[] arctanValue = new double[group.size()];
        for (int i = 0; i < arctanValue.length; i++) {
            int y = points[group.get(i)][1] - points[minimumY][1];
            int x = points[group.get(i)][0] - points[minimumY][0];
            arctanValue[i] = Math.atan(((double) y)/x);
        }
        for (int i = 0; i < group.size(); i++) {
            for (int j = i; j > 0; j--) {
                if (arctanValue[j] > arctanValue[j - 1]) {
                    Collections.swap(group, j -1, j);
                    double temp = arctanValue[j];
                    arctanValue[j] = arctanValue[j - 1];
                    arctanValue[j - 1] = temp;
                }
            }
        }
    }

    // main() for testing purposes
    public static void main(String[] args) {
        int[][] testPoints = {{3, 2}, {4, 0}, {0, -2}, {-2, 0}, {4, -1}, {-2, 4}, {3, 0}, {0, 0}};
        ConvexHull test1 = new ConvexHull(testPoints);
        test1.sort();
        System.out.println(test1.pointAddress);

        int[][] answer = test1.findConvexHull();
        for (int i = 0; i < answer.length; i++) {
            System.out.println("[" + answer[i][0] + ", " + answer[i][1] + "]");
        }

    }
}

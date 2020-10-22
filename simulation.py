# we will both plot random points in a graph
# and calculate the pi based on the ranomly plotted points
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# function that takes in the number of points n and makes that many of points in the 
# allPoints set, makes no repeats because its a set, also adds them to individual sets
# both in the circle and outside of it
def createSet(nPoints, xRange, yRange, allPoints):
    coordsInCircle = set()
    coordsOutsideOfCircle = set()

    for i in range(nPoints):
        x = random.uniform(0,xRange)
        y = random.uniform(0,yRange)

        allPoints.add((x,y))

        # calculates if the points are in the radius of the circle
        if x**2 + y **2 < 1:
            coordsInCircle.add((x,y))
        else:
            coordsOutsideOfCircle.add((x,y))

    # returns both sets made
    return coordsInCircle, coordsOutsideOfCircle


# checks error
def calcError(nSize, circleCords):
    estPi = (len(circleCords) / nSize) * 4

    errorVal = abs(((math.pi - estPi)*100)/ math.pi)

    print("with {0:} points, estimated pi is: {1:.6f}, error percentage is {2:.4f} %".format(nSize, estPi, errorVal))
    return estPi, errorVal


# plots the points in and outside of th circle
def plotGraph(circleCords, outCircleCords, errorVal, estPi):
    for point in circleCords:
        plt.scatter(point[0], point[1], .1, color='b')
    for point in outCircleCords:
        plt.scatter(point[0], point[1], .1, color='r')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Simulation Method: calculating pi " + str(round(estPi,6)) +" with error value: " + str(round(errorVal,4)) + "%") 
    plt.show()
    plt.close()


# runs the entire simulation and returns the graph with the points
def runSimulation(nPoints):
    xRange = 1
    yRange = 1
    allPoints = set()

    # creates the set in circle, total set and outside of the circle
    coordsInCircle, coordsOutsideOfCircle = createSet(nPoints, xRange, yRange, allPoints)

    # creates the pi and error value
    estPi, errorVal = calcError(nPoints, coordsInCircle)

    # plots the points on the graph
    plotGraph(coordsInCircle, coordsOutsideOfCircle, errorVal, estPi)


def main():
    nSize = 10 ** 3
    runSimulation(nSize)
    nSize = 10 ** 4
    runSimulation(nSize)
    nSize = 10 ** 5
    runSimulation(nSize)
    nSize = 10 ** 6
    runSimulation(nSize)

main()
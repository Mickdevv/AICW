import math
from numpy import genfromtxt


def main():
    class Node:
        def __init__(self, nodeNumber, visited, x, y, shortestFrom, tentDistance):
            self.nodeNumber = nodeNumber
            self.visited = visited
            self.x = x
            self.y = y
            self.shortestFrom = shortestFrom
            self.tentDistance = tentDistance

    text_file = genfromtxt("generated30-1.cav", delimiter=',')

    N = int(text_file[0])
    nodeList = []
    nodeMatrix = []
    distanceAcc = float(0)

    for a in range(N):
        # read all the nodes into the node list and matrix
        column = []
        nodeList.append(Node(int(a + 1), bool(False), float(text_file[a * 2 + 1]), float(text_file[a * 2 + 2]), 0, -1))
        for b in range(N):
            column.append(text_file[b + 2 * N + 1 + N * a])

        nodeMatrix.append(column)

    nodeList[0].tentDistance = 0
    destination = nodeList[-1]

    currentNode = nodeList[0]
    unvisitedNodes = nodeList
    distanceFromCurrent = []

    for i in range(3):  # start of the looping

        connectedTo = []
        print(currentNode.nodeNumber)
        for b in range(len(nodeMatrix)):  # creates a list of the node's neighbors and calculates their distances from the current node
            # print(nodeMatrix[currentNode.nodeNumber][b])
            if nodeMatrix[b][currentNode.nodeNumber - 1] == 1.0 and not nodeList[b].visited:
                distanceFromCurrentCalc = math.sqrt(
                    pow((currentNode.x - nodeList[b].x), 2) + pow((currentNode.y - nodeList[b].y), 2))
                distanceFromCurrent.append(distanceFromCurrentCalc)
                connectedTo.append(nodeList[b])


                if currentNode.tentDistance == -1:
                    currentNode.tentDistance = 0
                if nodeList[b].tentDistance + distanceFromCurrentCalc < currentNode.tentDistance:
                    nodeList[b].tentDistance = currentNode.tentDistance + distanceFromCurrentCalc

        if len(connectedTo) > 0:
            closestNode = connectedTo[0]
            for c in range(len(connectedTo)):  # identifies the closest node to the current node
                if closestNode.tentDistance > connectedTo[c].tentDistance:
                    closestNode = connectedTo[c]
            nodeList[currentNode.nodeNumber - 1].visited = True
            for a in range(len(connectedTo)):
                print(connectedTo[a].nodeNumber, connectedTo[a].tentDistance)

        currentNode = closestNode
        distanceAcc = distanceAcc + closestNode.tentDistance
        print(distanceAcc)
        print()
        unvisitedNodes = []
        for a in range(len(nodeList)):
            if not nodeList[a].visited:
                unvisitedNodes.append(nodeList[a])
    print("TD")
    for a in range(len(nodeList)):
        print(nodeList[a].tentDistance)

    #    for a in range(len(nodeMatrix)):
    #    print(nodeMatrix[a])


main()

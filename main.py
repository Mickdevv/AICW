import math
from numpy import genfromtxt


def main():
    class Node:
        def __init__(self, nodeNumber, visited, x, y, previousNode, tentDistance):
            self.nodeNumber = nodeNumber
            self.visited = visited
            self.x = x
            self.y = y
            self.previousNode = previousNode
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

    while len(unvisitedNodes) > 0:  # start of the looping

        connectedTo = []

        print(currentNode.nodeNumber)
        for b in range(len(
                nodeMatrix)):  # creates a list of the node's unvisited neighbors and calculates their distances from the current node
            # print(nodeMatrix[currentNode.nodeNumber][b])
            if nodeMatrix[b][currentNode.nodeNumber - 1] == 1.0 and not nodeList[b].visited:
                distanceFromCurrentCalc = math.sqrt(
                    pow((currentNode.x - nodeList[b].x), 2) + pow((currentNode.y - nodeList[b].y), 2))
                distanceFromCurrent.append(distanceFromCurrentCalc)
                connectedTo.append(nodeList[b])
                # Up to here everything seems to be fine

                # this for loop goes through the lists of connections and their distances and assigns the correct tentative values
        for a in range(len(connectedTo)):
            if connectedTo[a].tentDistance == -1 or nodeList[connectedTo[a].nodeNumber - 1].tentDistance > nodeList[currentNode.nodeNumber - 1].tentDistance + distanceFromCurrent[a]:
                nodeList[connectedTo[a].nodeNumber - 1].tentDistance = nodeList[currentNode.nodeNumber - 1].tentDistance + distanceFromCurrent[a]
                nodeList[connectedTo[a].nodeNumber - 1].previousNode = currentNode.nodeNumber

        if len(connectedTo) > 0:
            closestNode = nodeList[connectedTo[0].nodeNumber-1]
            for c in range(len(connectedTo)):  # identifies the closest node to the current node
                if closestNode.tentDistance > nodeList[connectedTo[c].nodeNumber-1].tentDistance:
                    closestNode = nodeList[connectedTo[c].nodeNumber-1]
            nodeList[currentNode.nodeNumber - 1].visited = True
            for a in range(len(connectedTo)):
                print(connectedTo[a].nodeNumber, connectedTo[a].tentDistance)
        else:
            print("irvbeiurbeiuriuerfn")
            for a in range(len(nodeList)):
                distanceFromCurrent = []
                connectedTo = []
                print(1)
                for b in range(len(
                        nodeMatrix)):  # creates a list of the node's unvisited neighbors and calculates their distances from the current node
                    # print(nodeMatrix[currentNode.nodeNumber][b])
                    print(2)

                    if nodeMatrix[b][currentNode.nodeNumber - 1] == 1.0 and not nodeList[b].visited:
                        distanceFromCurrentCalc = math.sqrt(
                            pow((currentNode.x - nodeList[b].x), 2) + pow((currentNode.y - nodeList[b].y), 2))
                        distanceFromCurrent.append(distanceFromCurrentCalc)
                        connectedTo.append(nodeList[b])
                        print(3)
                if nodeList[a].visited == True and len(connectedTo) > 0:
                    currentNode = nodeList[a]
                    print(4)
                    break
                print()


        nodeList[currentNode.nodeNumber - 1].visited = True
        currentNode = closestNode
        print()
        unvisitedNodes = []
        for a in range(len(nodeList)):
            if not nodeList[a].visited:
                unvisitedNodes.append(nodeList[a])

    print("TD")
    for a in range(len(nodeList)):
        print(nodeList[a].nodeNumber, nodeList[a].previousNode, nodeList[a].tentDistance)

    #    for a in range(len(nodeMatrix)):
    #    print(nodeMatrix[a])


main()

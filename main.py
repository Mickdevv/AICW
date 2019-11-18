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

    # Up to here all has been reading in from the file and sorting the information into the appropriate format for
    # the program to deal with

    while len(unvisitedNodes) > 0:  # start of the looping

        connectedTo = []
        distanceFromCurrent = []

        for b in range(len(nodeMatrix)):  # creates a list of the node's neighbors and calculates their distances from the current node
            # print(nodeMatrix[currentNode.nodeNumber][b])
            if nodeMatrix[b][currentNode.nodeNumber - 1] == 1.0:
                distanceFromCurrentCalc = math.sqrt(pow((currentNode.x - nodeList[b].x), 2) + pow((currentNode.y - nodeList[b].y), 2))
                distanceFromCurrent.append(distanceFromCurrentCalc)
                connectedTo.append(nodeList[b])
                # Up to here everything seems to be fine

                if nodeList[b].tentDistance > currentNode.tentDistance + distanceFromCurrentCalc or nodeList[b].tentDistance == -1:
                    nodeList[b].tentDistance = currentNode.tentDistance + distanceFromCurrentCalc
        ########################################################################################################################

        # for i in range(len(nodeList)):
            # print(nodeList[i].nodeNumber, nodeList[i].tentDistance)

        for a in range(len(connectedTo)):
            if not nodeList[connectedTo[a].nodeNumber-1].visited:
                hasUnvisitedNeighbors = True
                break
            else:
                hasUnvisitedNeighbors = False

        if hasUnvisitedNeighbors:
            print()
            print("*****IF*****")
            print(currentNode.nodeNumber)
            # this for loop goes through the lists of connections and their distances and assigns the correct tentative values
            for a in range(len(connectedTo)):
                if nodeList[connectedTo[a].nodeNumber - 1].tentDistance == -1 or nodeList[connectedTo[a].nodeNumber - 1].tentDistance > nodeList[currentNode.nodeNumber - 1].tentDistance + distanceFromCurrent[a]:
                    nodeList[connectedTo[a].nodeNumber - 1].tentDistance = nodeList[currentNode.nodeNumber - 1].tentDistance + distanceFromCurrent[a]
                    nodeList[connectedTo[a].nodeNumber - 1].previousNode = currentNode.nodeNumber

            for a in range(len(connectedTo)):
                if not nodeList[connectedTo[a].nodeNumber-1].visited:
                    closestNode = nodeList[connectedTo[a].nodeNumber-1]
                    closestNodeIndex = a
                    break
            for c in range(len(connectedTo)):  # identifies the closest unvisited node to the current node
                if distanceFromCurrent[closestNodeIndex] > distanceFromCurrent[c] and not nodeList[connectedTo[c].nodeNumber - 1].visited:
                    closestNodeIndex = c
            closestNode = nodeList[connectedTo[closestNodeIndex].nodeNumber-1]

            nodeList[currentNode.nodeNumber - 1].visited = True
            for a in range(len(connectedTo)):
                if not connectedTo[a].visited:
                    print(connectedTo[a].nodeNumber, distanceFromCurrent[a])

        else:  # Goes through the list of nodes and finds a visited node with an unvisited neighbor and starts from there
            print()
            print("*****ELSE*****")
            print(currentNode.nodeNumber)
            connectedTo = []
            distanceFromCurrent = []
            nodeList[currentNode.nodeNumber - 1].visited = True

            for a in range(len(nodeList)):
                for b in range(len(nodeMatrix)):
                    if nodeMatrix[b][nodeList[a].nodeNumber - 1] == 1.0:  # looks for connections
                        distanceFromCurrentCalc = math.sqrt(pow((nodeList[a].x - nodeList[b].x), 2) + pow((nodeList[a].y - nodeList[b].y), 2))
                        distanceFromCurrent.append(distanceFromCurrentCalc)
                        connectedTo.append(nodeList[b])

                        if nodeList[b].tentDistance > nodeList[a].tentDistance + distanceFromCurrentCalc or nodeList[b].tentDistance == -1:
                            nodeList[b].tentDistance = nodeList[a].tentDistance + distanceFromCurrentCalc

                if len(connectedTo) > 0:
                    for b in range(len(distanceFromCurrent)):
                        if not nodeList[connectedTo[b].nodeNumber - 1].visited:
                            closestNodeIndex = b
                            hasUnvisitedNeighbors = True
                            break
################################################ something wrong here #################################################
                    print(len(distanceFromCurrent))
                    print(closestNodeIndex)
                    for c in range(len(distanceFromCurrent)):  # identifies the closest node to the current node
                        if distanceFromCurrent[closestNodeIndex] > distanceFromCurrent[c] and not nodeList[connectedTo[c].nodeNumber - 1].visited:
                            closestNodeIndex = c
                            print(closestNodeIndex)
                    closestNode = nodeList[connectedTo[closestNodeIndex].nodeNumber-1]

################################################ something wrong here #################################################
                    nodeList[currentNode.nodeNumber - 1].visited = True
                    for d in range(len(connectedTo)):
                        if not nodeList[connectedTo[d].nodeNumber-1].visited:
                            print(connectedTo[d].nodeNumber, connectedTo[d].tentDistance)
                    if hasUnvisitedNeighbors:
                        break

        currentNode = closestNode
        print()
        unvisitedNodes = []
        print("Unvisited Nodes")
        for a in range(len(nodeList)):
            if not nodeList[a].visited:
                unvisitedNodes.append(nodeList[a])
                print(nodeList[a].nodeNumber)

    print("TD")
    for a in range(len(nodeList)):
        print(nodeList[a].nodeNumber, nodeList[a].previousNode, nodeList[a].tentDistance)
    a = 24
    while a != 0:
        print(nodeList[a].nodeNumber)
        a = nodeList[a].previousNode - 1
    print(nodeList[0].nodeNumber)
    print()
    print(nodeList[N - 1].tentDistance)
    #    for a in range(len(nodeMatrix)):
    #    print(nodeMatrix[a])


main()

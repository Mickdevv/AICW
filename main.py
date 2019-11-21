import math
import time
from numpy import genfromtxt


def main():
    start_time = time.time()

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
    previousStartingPoint = 0

    hasUnvisitedNeighbours = True
    allNodesVisited = False
    currentNode = nodeList[0]

    # Up to here all has been reading in from the file and sorting the information into the appropriate format for
    # the program to deal with

    while not allNodesVisited:  # start of the looping
        print(0)
        connectedTo = []
        distanceFromCurrent = []
        print(hasUnvisitedNeighbours)
        for b in range(len(nodeMatrix)):  # creates a list of the node's neighbors and calculates their distances from the current node
            # print(nodeMatrix[currentNode.nodeNumber][b])
            if nodeMatrix[b][currentNode.nodeNumber - 1] == 1.0:
                distanceFromCurrentCalc = math.sqrt(pow((currentNode.x - nodeList[b].x), 2) + pow((currentNode.y - nodeList[b].y), 2))
                distanceFromCurrent.append(distanceFromCurrentCalc)
                connectedTo.append(nodeList[b])
                # Up to here everything seems to be fine

                if nodeList[b].tentDistance > currentNode.tentDistance + distanceFromCurrentCalc or nodeList[b].tentDistance == -1:
                    nodeList[b].tentDistance = currentNode.tentDistance + distanceFromCurrentCalc
                    nodeList[b].previousNode = currentNode.nodeNumber
        ########################################################################################################################

        # for i in range(len(nodeList)):
            # print(nodeList[i].nodeNumber, nodeList[i].tentDistance)
        print ("UNVN 1")
        for a in range(len(connectedTo)):
            print (nodeList[connectedTo[a].nodeNumber - 1].visited)
        print("UNVN 1")

        for a in range(len(connectedTo)):

            if len(connectedTo) == 0:
                hasUnvisitedNeighbours = False
                break
            elif not nodeList[connectedTo[a].nodeNumber-1].visited:
                hasUnvisitedNeighbours = True
                break
            else:
                hasUnvisitedNeighbours = False

        print(hasUnvisitedNeighbours)
        if hasUnvisitedNeighbours and len(connectedTo) > 0:
            print("***IF***")
            # this for loop goes through the lists of connections and their distances and assigns the correct tentative values
            closestNodeIndex = 0
            for a in range(len(connectedTo)):
                if nodeList[connectedTo[a].nodeNumber - 1].tentDistance == -1 or nodeList[connectedTo[a].nodeNumber - 1].tentDistance > nodeList[currentNode.nodeNumber - 1].tentDistance + distanceFromCurrent[a]:
                    nodeList[connectedTo[a].nodeNumber - 1].tentDistance = nodeList[currentNode.nodeNumber - 1].tentDistance + distanceFromCurrent[a]
                    # nodeList[connectedTo[a].nodeNumber - 1].previousNode = currentNode.nodeNumber

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
            print("***END IF***")
        else:  # Goes through the list of nodes and finds a visited node with an unvisited neighbor and starts from there
            print("***ELSE***")
            print ()
            print (currentNode.nodeNumber)
            connectedTo = []
            distanceFromCurrent = []
            nodeList[currentNode.nodeNumber - 1].visited = True
            print(1)
            for a in range(previousStartingPoint, len(nodeList)):
                # print(previousStartingPoint)
                previousStartingPoint = a
                closestNodeIndex = 0
                for b in range(len(nodeMatrix)):
                    # print(2)
                    if nodeMatrix[b][nodeList[a].nodeNumber - 1] == 1.0:  # looks for connections
                        distanceFromCurrentCalc = math.sqrt(pow((nodeList[a].x - nodeList[b].x), 2) + pow((nodeList[a].y - nodeList[b].y), 2))
                        distanceFromCurrent.append(distanceFromCurrentCalc)
                        connectedTo.append(nodeList[b])

                        if nodeList[b].tentDistance > nodeList[a].tentDistance + distanceFromCurrentCalc or nodeList[b].tentDistance == -1:
                            nodeList[b].tentDistance = nodeList[a].tentDistance + distanceFromCurrentCalc
                            nodeList[b].previousNode = nodeList[a].nodeNumber
                print("Length connectedTo")
                print(len(connectedTo))
                print("UNV 2")
                for death in range(len(connectedTo)):
                    print(connectedTo[death].visited)
                print("UNV 2")

                if len(connectedTo) > 0:
                    for b in range(len(connectedTo)):
                        # print (3)
                        if not nodeList[connectedTo[b].nodeNumber - 1].visited:
                            closestNodeIndex = b
                            hasUnvisitedNeighbours = True
                            print ("break1")
                            break

                    for c in range(len(distanceFromCurrent)):  # identifies the closest node to the current node
                        if distanceFromCurrent[closestNodeIndex] > distanceFromCurrent[c] and not nodeList[connectedTo[c].nodeNumber - 1].visited:
                            closestNodeIndex = c

                    closestNode = nodeList[connectedTo[closestNodeIndex].nodeNumber-1]
                    nodeList[currentNode.nodeNumber - 1].visited = True

                if hasUnvisitedNeighbours:
                    print("break2")
                    break
                print("***END ELSE***")


        # nodeList[currentNode.nodeNumber-1].previousNode = currentNode.nodeNumber
        print("Current, Closest")
        print(currentNode.nodeNumber)
        print(closestNode.nodeNumber)
        currentNode = closestNode
        for a in range(len(nodeList)):
            if not nodeList[a].visited:
                allNodesVisited = False
                break
            else:
                allNodesVisited = True

        unvisitedNodes = []
        for a in range(len(nodeList)):
            if not nodeList[a].visited:
                unvisitedNodes.append(nodeList[a])

    print("TD")
    for a in range(len(nodeList)):
        print(nodeList[a].nodeNumber, nodeList[a].previousNode, nodeList[a].tentDistance)

    path = []
    a = N
    duplicates = False
    f = open("myfile.txt", "w")
    while a != 0 and not duplicates:
        path.append(nodeList[a-1].nodeNumber)
        a = nodeList[a-1].previousNode
        if len(path) > N:
            duplicates = True

    if duplicates:
        print("No path found")
    else:
        path.reverse()
        print(path)
        for i in range(len(path)):
            f.write(str(path[i]) + ", ")
        print(nodeList[N-1].tentDistance)
        f.write("Path length: " + str(nodeList[N-1].tentDistance))
        f.write(" Time Taken: %s seconds" % (time.time() - start_time))
    print("--- %s seconds ---" % (time.time() - start_time))


main()

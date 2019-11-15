from numpy import genfromtxt


def main():
    class Node:
        def __init__(self, nodeNumber, visited, x, y, tentDistance):
            self.nodeNumber = nodeNumber
            self.visited = visited
            self.x = x
            self.y = y
            self.tentDistance = tentDistance

    text_file = genfromtxt("generated30-1.cav", delimiter=',')

    N = int(text_file[0])
    nodeList = []
    nodeMatrix = []

    for a in range(N):
        column = []
        nodeList.append(Node(int(a + 1), bool(False), float(text_file[a * 2 + 1]), float(text_file[a * 2 + 2]), -1))
        for b in range(N):
            column.append(text_file[b + 2 * N + 1 + N * a])

        nodeMatrix.append(column)

    nodeList[0].tentDistance = 0
    firstNode = nodeList[2]
    destination = nodeList[-1]
    connectedTo = []

    currentNode = firstNode
    unvisitedNodes = nodeList
    for b in range(len(nodeMatrix)):
        # print(nodeMatrix[currentNode.nodeNumber][b])
        if nodeMatrix[b][currentNode.nodeNumber - 1] == 1.0:
            tentDistanceCalc = pow((pow((nodeList[b].x-currentNode.x), 2) + pow((nodeList[b].y-currentNode.y), 2)), 0.5)
            nodeList[b].tentDistance = tentDistanceCalc
            connectedTo.append(nodeList[b])
    closestNode = connectedTo[0]
    for c in range(len(connectedTo)):
        if closestNode.tentDistance > connectedTo[c].tentDistance:
            closestNode = connectedTo[c]



    # for a in range(len(nodeMatrix)):
    #    print(nodeMatrix[a])

    for a in range(len(connectedTo)):
        print(connectedTo[a].nodeNumber)
        print(connectedTo[a].tentDistance)

    print()
    print(closestNode.nodeNumber)


main()

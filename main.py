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
        nodeList.append(Node(int(a), bool(False), int(text_file[a * 2 + 1]), int(text_file[a * 2 + 2]), -1))
        for b in range(N):
            column.append(text_file[a + b + 2 * N + 1])

        nodeMatrix.append(column)

    nodeList[0].tentDistance = 0
    firstNode = nodeList[0]
    destination = nodeList[-1]
    connectedTo = []

    currentNode = firstNode
    unvisitedNodes = nodeList
    for b in range(len(nodeMatrix)):
        # print(nodeMatrix[currentNode.nodeNumber][b])
        if nodeMatrix[currentNode.nodeNumber][b] == 1.0:
            connectedTo.append(nodeList[b])
    for a in range(len(nodeMatrix)):
        print(nodeMatrix[a])

    print(connectedTo)


main()

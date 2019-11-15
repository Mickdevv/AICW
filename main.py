
from numpy import genfromtxt


def FileImport():
    class Node:
        def __init__(self, visited, nodeNumber, x, y):
            self.nodeNumber = nodeNumber
            self.visited = visited
            self.x = x
            self.y = y

    text_file = genfromtxt("generated30-1.cav", delimiter=',')

    N = int(text_file[0])
    nodeList = []
    nodeMatrix = []

    for a in range(N):
        column = []
        nodeList.append(Node(int(a), bool(False), int(text_file[a * 2 + 1]), int(text_file[a * 2 + 2])))
        for b in range(N):
            column.append(text_file[a + b + 2 * N + 1])

        nodeMatrix.append(column)


def main():
    FileImport()


main()


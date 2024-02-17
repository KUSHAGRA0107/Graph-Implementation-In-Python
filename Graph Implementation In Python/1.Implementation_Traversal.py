class Graph:
    def __init__(self, vertices, edgecount):
        self.vertices, self.edges = vertices, edgecount
        self.adjacencyMatrix = [[0 for i in range(self.vertices)] for i in range(self.vertices)]  # 2D Array
        self.adjacencyList = [[] for i in range(self.vertices)]  # List

    def createAdjacencyMatrix(self, edgeList):
        for i in range(len(edgeList)):
            u, v = edgeList[i]
            self.adjacencyMatrix[u][v] = 1
            self.adjacencyMatrix[v][u] = 1

    def createAdjacencyList(self, edgeList):
        for i in range(len(edgeList)):
            u, v = edgeList[i]
            self.adjacencyList[u].append(v)
            self.adjacencyList[v].append(u)

    def bfs(self, startNode):
        answer = []
        queue = []
        visited_array = [0] * self.vertices
        queue.append(startNode)
        visited_array[startNode] = 1

        while len(queue) != 0:
            popped = queue.pop(0)
            answer.append(popped)

            for i in self.adjacencyList[popped]:
                if not visited_array[i]:
                    visited_array[i] = 1
                    queue.append(i)

        print(answer)

    def dfs(self, node):
        visited_array = [0] * self.vertices
        answer = []
        self.__dfsSearch(0, visited_array, self.adjacencyList, answer)
        print(answer)

    def __dfsSearch(self, node, visited_array, adjacencyList, answer):
        answer.append(node)
        visited_array[node] = 1

        for i in self.adjacencyList[node]:
            if not visited_array[i]:
                self.__dfsSearch(i, visited_array, adjacencyList, answer)


if __name__ == "__main__":
    graph = Graph(6, 9)
    edges = [[1, 2], [1, 3], [2, 4], [2, 3], [3, 4], [3, 5], [4, 5], [4, 0], [5, 0]]
    graph.createAdjacencyMatrix(edges)
    graph.createAdjacencyList(edges)
    graph.bfs(0)
    graph.dfs(0)

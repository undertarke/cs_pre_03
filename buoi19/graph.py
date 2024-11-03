class Graph:
    def __init__(self):
        self.graph = { }

    def addVertex(self, vertex1, vertex2):

        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        # dùng cho đồ thị vô hướng
        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]

    def getNeighbour(self,vertex):
        return self.graph[vertex]
    

    def dfs(self,keyStart,visited=None):
        if visited is None:
            visited = set()

        visited.add(keyStart)
        print(keyStart)
        for neighbour in self.graph.get(keyStart,[]):
            if neighbour not in visited:
                self.dfs(neighbour,visited)

        
        
    
graph = Graph()

graph.addVertex(1,2)
graph.addVertex(1,3)
graph.addVertex(2,3)
graph.addVertex(2,4)
graph.addVertex(3,5)
graph.addVertex(4,5)
graph.addVertex(5,6)
graph.addVertex(6,7)
graph.addVertex(7,8)
graph.addVertex(7,9)

# print(graph.getNeighbour(7))
graph.dfs(1)

# print(str(graph.graph))



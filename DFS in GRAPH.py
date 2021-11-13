class Graph:
    def __init__(self, vertices):
        self.map = {}
        self.V = vertices
        for i in range(vertices):
            self.map[i] = []
    
    def addEdge(self, u, v):
        self.map[u].append(v)
    
    def DFS_Util(self, v, visited):
        visited.add(v)
        print(v, end = ' ')
        for neighbour in self.map[v]:
            if neighbour not in visited:
                self.DFS_Util(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFS_Util(v, visited)

g = Graph(6)
g.addEdge(0, 4) 
g.addEdge(1, 2) 
g.addEdge(1, 0) 
g.addEdge(2, 1) 
g.addEdge(2, 4) 
g.addEdge(3, 1)
g.addEdge(3, 2) 
g.addEdge(4, 3) 
g.addEdge(3, 5) 

g.DFS(2)
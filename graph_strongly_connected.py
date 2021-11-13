class Graph:
    def __init__(self,vertices):
        self.map = {} # adjacency list
        self.V= vertices # count of vertices 
        for index in range(vertices):
            # initialise map with empty list
            self.map[index] = []     
            
    # Function to add an edge to graph
    def addEdge(self, u, v):
         #Add w to v list 
        self.map[u].append(v)

    def assignment_checkConnected(self):
        N = self.V
        for i in range(0, N):
            visited = [False]*N
            self.depth_first(i, visited)
            for b in visited:
                if b == False:
                    return False
        return True

    def depth_first(self, v:int, visited):
        visited[v] = True
        for u in self.map.get(v):
            if (visited[u] == False):
                self.depth_first(u, visited)


g = Graph(5)
g.addEdge(0, 4) 
g.addEdge(1, 2) 
g.addEdge(1, 0) 
g.addEdge(2, 1) 
g.addEdge(2, 4) 
g.addEdge(3, 1)
g.addEdge(3, 2) 
g.addEdge(4, 3) 

res = g.assignment_checkConnected()
print(res)
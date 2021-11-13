from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def DFS(self, v, visited, parent = -1):
        visited[v] = 1
        for i in self.graph[v]:
            if parent != -1 and i == parent:
                continue
            if visited[i]:
                return 'Cycle Found'
            return self.DFS(i, visited, v)
        return 'No Cycles found'
    
if __name__=='__main__':
    g = Graph()
    g.addEdge(1, 0) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(0, 3) 
    g.addEdge(3, 4) 
    visited = defaultdict(int)
    for i in g.graph:
        if not visited[i]:
            status = g.DFS(i, visited)
    print(status)
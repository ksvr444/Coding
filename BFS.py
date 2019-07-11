class Graph:
    def __init__(self, val):
        self.adj = [[] for _ in range(val)]

    def addEdge(self, nd, nnd):
        self.adj[nd].append(nnd)
        
    def bfs(self, val):
        visited = [False]*len(self.adj)
        al = []
        al.append(val)
        visited[val] = True
        while al:
            x = al.pop(0)
            print(x)
            temp = self.adj[x]
            print("in", temp)
            for val in temp:
                if not visited[val]: 
                    al.append(val)
                    visited[val] = True 
                
                

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bfs(2)

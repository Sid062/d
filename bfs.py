from collections import defaultdict,deque
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,start):
        visited=set()
        queue=deque()

        visited.add(start)
        queue.append(start)

        while queue:
            vertex=queue.popleft()
            print(vertex,end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in  visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g=Graph()

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('C','F')

print("Breadth first search starting from vertex 'A' : ")
g.bfs('A')
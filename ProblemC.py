from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, u, v, weight, color):
        self.graph.append([u - 1, v - 1, weight, color])

    def findSet(self, x, parent):
        if x != parent[x]: parent[x] = self.findSet(parent[x], parent)
        return parent[x]

    def link(self, x, y, parent, rank):
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    def union(self, x, y, parent, rank):
        self.link(self.findSet(x, parent), self.findSet(y, parent), parent, rank)

    def sortEdges(self, graph):
        reds = []
        blues = []
        for u, v, weight, color in graph:
            if color == 'red':
                reds.append([u, v, weight, color])
            else:
                blues.append([u, v, weight, color])

        reds = sorted(reds, key = lambda item: item[2], reverse = True)
        blues = sorted(blues, key = lambda item: item[2], reverse = True)

        return reds + blues

    def kruskal(self):
        A = []
        parent = []
        rank = []

        redHappiness = 0
        blueHapiness = 0

        for v in range(self.vertices):
            parent.append(v)
            rank.append(0)

        self.graph = self.sortEdges(self.graph)

        for u, v, weight, color in self.graph:
            if self.findSet(u, parent) != self.findSet(v, parent):
                if color == 'red':
                    redHappiness += weight
                else:
                    blueHapiness += weight

                A.append([u, v, weight, color])
                self.union(u, v, parent, rank)

        return redHappiness, blueHapiness

def main():
    str_n, str_m = input().split()
    n = int(str_n)
    m = int(str_m)

    g = Graph(n)

    for i in range(m):
        str_e1, str_e2, str_hap, color = input().split()
        e1 = int(str_e1)
        e2 = int(str_e2)
        hap = int(str_hap)

        g.addEdge(e1, e2, hap, color)
    
    print(g.kruskal()[0], g.kruskal()[1], '\n')

if __name__ == "__main__":
    main()
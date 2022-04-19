from collections import defaultdict
from itertools import combinations

def minGoldBFS(graph, s, t):
    if graph[t] == [] and len(graph) > 1 and s != t:
        return 'Impossible'
        
    distances = [None] * (len(graph)) 
    distances[s] = 0

    queue = []
    queue.append(s)

    while queue:
        u = queue.pop(0)
        if u == t:
            return distances[u]

        for v in graph[u]:
            if distances[v] == None:
                
                distances[v] = distances[u] + 1
                queue.append(v)
        
    return 'Impossible'

def main():
    str_n, str_m, str_k, str_s, str_t = input().split()

    n = int(str_n)
    m = int(str_m)
    k = int(str_k)
    s = int(str_s)
    t = int(str_t)

    g = []
    for i in range(n+1):
        g.append([])

    a = input().split()
    for i in range(k):
        g[n].append(int(a[i]) - 1)
        g[int(a[i]) - 1].append(n)

    for i in range(m):
        v1, v2 = input().split()
        u = int(v1) - 1
        v = int(v2) - 1
        g[u].append(v)
        g[v].append(u)

    print(minGoldBFS(g, s - 1, t - 1), '\n')

if __name__ == "__main__":
    main()
from sys import stdin
from collections import deque
def dfs(graph, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()
        print(node)
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

m, n = map(int, stdin.readline().split())
b = [list(map(int, stdin.readline().split()[:m])) for _ in range(n)]
b.insert(0,[])
print(dfs(b, 1))

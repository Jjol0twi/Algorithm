import sys

def build_tree(edges):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    parent = {1: None}
    queue = [1]
    for node in queue:
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return parent

input = sys.stdin.readline
n = int(input())
edges = []
for _ in range(n-1):  # 예시에서는 6개의 간선
    a, b = map(int, input().split())
    edges.append((a, b))
tree = build_tree(edges)
for i in range(2,n+1):
    print(tree[i])

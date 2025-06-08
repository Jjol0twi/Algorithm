from sys import stdin

input = stdin.readline

def min_moves(N, r1, c1, r2, c2):
    visited = [[False] * N for _ in range(N)]

    dr = [-2, -2, 0, 0, 2, 2]
    dc = [-1, 1, -2, 2, -1, 1]

    queue = [(r1, c1, 0)]
    visited[r1][c1] = True

    index = 0
    while index < len(queue):
        r, c, moves = queue[index]
        index += 1

        if r == r2 and c == c2:
            return moves

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, moves + 1))

    return -1

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

print(min_moves(N, r1, c1, r2, c2))

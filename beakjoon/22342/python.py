import sys
input = sys.stdin.readline

m, n  = map(int, input().split())   # 가로, 세로 줄 입력
weights = [[int(char) for char in input().strip()] for _ in range(m)]   # 가중치 입력
out_values = {}     # 출력 값 저장

def getMaxOutValue(i, j):   # 재귀로 출력값 계산
    if (i,j) in out_values: # 이전 출력 값 있으면 호출
        return out_values[(i,j)]
    if j < 0 or i < 0 or i >= m:    # 범위에 안 맞으면 0 반환
        return 0
    if j == 0:              # 0열 일 경우 가중치 반환( + 0)
        out_values[(i,j)] = weights[i][j]
        return out_values[(i,j)]
    prev_outputs = []       # (x-1, y) (x-1, y+1) (x-1, y-1) 값 구하기
    for di in [-1, 0, 1]:
        prev_i = i + di
        prev_j = j - 1
        if 0 <= prev_i < m:
            prev_outputs.append(getMaxOutValue(prev_i, prev_j))
    max_output = max(prev_outputs) if prev_outputs else 0
    out_values[(i,j)] = max_output + weights[i][j]
    return out_values[(i,j)]

# 모든 위치의 저장값 중 최댓값 구하기
max_stored = 0
for i in range(m):
    for j in range(n):
        stored_val = getMaxOutValue(i, j) - weights[i][j]  # 저장값 = 출력값 - 가중치
        max_stored = max(max_stored, stored_val)
print(max_stored)

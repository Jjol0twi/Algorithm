from sys import stdin
# t = int(stdin.readline())
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()[:n]))
    odd_count = sum(x&1 for x in a)
    if odd_count * 2 == n:  # 홀수와 짝수의 개수가 같은 경우
        print("heeda0528")
    else:
        max_count = max(odd_count, n - odd_count)   # 만약 두 선수 같은 유형의 카드를 골랐을 때
        print("amsminn" if max_count & 1 else "heeda0528")

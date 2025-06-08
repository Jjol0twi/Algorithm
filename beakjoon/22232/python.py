import sys
n, m = map(int, sys.stdin.readline().split())   # n m 입력
fl = [sys.stdin.readline().strip().split('.') for _ in range(n)]    # 1~n+1번째 파일명 입력
fe = set(sys.stdin.readline().strip() for _ in range(m))    # n+1~까지 확장자 입력
fl = sorted(fl, key=lambda x: (x[0], x[1] not in fe, x[1])) # 파일명, 확장자 있는지, 확장자 순으로 정렬
for i in fl:
    print(f"{i[0]}.{i[1]}")

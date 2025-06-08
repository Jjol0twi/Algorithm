import sys
from collections import Counter

answer = [0,0]
n, m, b = map(int, sys.stdin.readline().split()) # 입력 1
elev = [list(map(int, sys.stdin.readline().split()[:m])) for _ in range(n)]  # 입력 2
min_height = min(map(min, elev))    # 최소 높이
max_height = max(map(max, elev))    # 최대 높이
total_blocks = sum(sum(elev,[]))    # 설치된 블록 총 수
dic_box = Counter() # 입력 받은 수 dic으로 변경 k(숫자):v(숫자 중복 개수)
for i in elev:
    dic_box += Counter(i)
for i in range(min_height,max_height+1):
    if i*(n*m) <= sum(sum(elev,[]))+b:
        p = [0,i]
        for k, v in dic_box.items():
            if k!=i:
                j = k-i
                if j < 0:
                    p[0]+=abs(j)*v
                else:
                    p[0]+=j*2*v
        if answer[0]>=p[0] or answer[0]==0:
            answer=p
print(answer[0],answer[1])

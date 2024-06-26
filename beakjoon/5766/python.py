import sys
from collections import Counter
while True:
    n, m = list(map(int, sys.stdin.readline().split())) # n m 입력 받기
    if n==0 and m==0:   # n m 0 0으로 입력 시 탈출
        break
    c = Counter()  # 카운터 선언
    for i in range(n):
        ri = list(map(int, sys.stdin.readline().split()))
        c.update(ri[:m])  # 각 줄의 처음 m개의 숫자만 카운트
    sc = sorted(c.items(), key=lambda x: (-x[1], x[0]))  # 결과 정렬
    s = 0
    for i in range(m):
        s = sc[i][1]
        if sc[0][1] > s:
            break
    answer = [item[0] for item in sc if item[1] == s]  # 두번째로 많이 중복된 숫자 찾기
    print(' '.join(map(str, answer)))
    # ri = {} # dic 선언
    # for i in range(n):  # n번 반복
    #     tc = list(map(int, sys.stdin.readline().split()))   # n행 상위 m명의 랭킹 정보
    #     for j in range(m):
    #         if not tc[j] in ri: # ri에 선수 번호 추가
    #             ri[tc[j]] = 1
    #         else:
    #             ri[tc[j]]+=1    # 이미 존재한다면 value 1 추가
    # ri = sorted(ri.items(), key=lambda x: (-x[1], x[0]))    # value 내림차순, key 오름차순 정렬
    # s, l = 0, 0 # 두번째 값, 제일 큰 값
    # for i in range(len(ri)):
    #     if ri[i][1] > l:    # 제일 큰 값보다 크면 l = ri[i][1], s = l
    #         s = l
    #         l = ri[i][1]
    #     elif s < ri[i][1] < l:  # s 값일 때
    #         s = ri[i][1]
    # for i in range(len(ri)):    # s 값일 때 출력
    #     if ri[i][1]==s:
    #         print(ri[i][0], end=" ")
    # print() # 줄 바꿈

import sys
k=int(sys.stdin.readline()) # k 입력
cr = []   # k번째 (p m t j) * n 저장소
for i in range(k):  # input &
    m, n, p = map(int,sys.stdin.readline().split()) # k번째 m, n, p 입력
    tc = [list(map(lambda x: int(x) if x.isdigit() else x, sys.stdin.readline().split())) for j in range(n)]    # n번 4개씩 입력 + int int str int 형식
    tc.sort(key=lambda x: (-x[3], x[2])) # p(오), j(내), t(오) 순으로 정렬
    kcr={}   # dictionary로 구현
    for j in range(p):  # p 만큼 key 만들기
        kcr[j+1] = {}
    for j in tc:
        # if not j[0] in kcr:
        #     kcr[j[0]] = {}
        if not j[1] in kcr[j[0]] and j[3] and 65 <= ord(j[1]) < 65+m:   # 문제 번호 key 만들기 & j일때만
            kcr[j[0]][j[1]] = j[2]
        if j[1] in kcr[j[0]] and not j[3]:   # 문제 틀린 횟수*20
            kcr[j[0]][j[1]] += 20
    kcr=[[id, len(values), sum(values.values())] for id, values in kcr.items()]   # [참가자, 맞힌 문제 수, 총 점수]
    kcr.sort(key=lambda x: (-x[1], x[2], x[0]))  # 맞힌 문제 수, 총 점수 순으로 정렬
    cr.append(kcr)   # cr에 추가
for i in range(k):  # output
    print("Data Set {}:".format(i+1))
    for j in cr[i]:
        print(' '.join(map(str,j)))
    if i<k-1:
        print()

from sys import stdin
n, a, b, m = map(int, stdin.readline().split()) # 학생 수, j 위치, 만족하는 거리, 총 주
sl, r, cr, h = [[0, k] for k in range(n)], 0, 0, 0    # 위치 : [점수 , 학번], 결과 값, 연속된 결과 값, h 위치, 점수를 주는 주(총 주 -1)
for i in range(m):  # 점수를 주는 주만큼 반복
    if abs(h - a) <= b:
        r += 1
        cr += 1
    else:
        cr = 0
    if i==m-1:
        break
    isc = [list(map(int, stdin.readline().split()[:n])) for _ in range(2)]  # 이번주 상점 벌점 입력
    scm = [a - b for a, b in zip(isc[0], isc[1])]   # 이번주 상벌점 총합
    for j in range(n):
        sl[j][0]+=scm[sl[j][1]] # 학번에 맞춰서 총 상벌점 계산
    for j in range(n-1):
        fs, bs = sl[j][0], sl[j+1][0]
        if fs>=0: # 앞 방의 점수가 양의 정수일 때
            if fs+2<=bs:   # 앞 방이 뒷 방의 점수보다 2점 이상 높을 때
                sl[j], sl[j+1] = sl[j+1], sl[j]
            else:
                continue
        else:           # 앞 방의 점수가 음의 정수일 때
            if fs+4<=bs:   # 앞 방이 뒷 방의 점수보다 4점 이상 높을 때
                sl[j], sl[j+1] = sl[j+1], sl[j]
            else:
                continue
        sl[j][0], sl[j+1][0] = sl[j][0]-2, sl[j+1][0]+2 # 방 교체 시 급격한 변동 방지
        if h == j + 1:
            h = j
        elif h == j:
            h = j + 1
        if a == j + 1:
            a = j
        elif a == j:
            a = j + 1
print(r,cr)

cardNum = int(input())  # n 입력
sanggeun = []   # 상근이 리스트 선언
for i in range(cardNum):    # n만큼 상근이 수 받기
    sanggeun.append(int(input()))
sanggeun.sort() # 상근이 리스트
geunsang = sorted([i for i in range(1, cardNum*2+1) if i not in sanggeun])  # 근상이 수 받기
now=0   # 현재 테이블에 올려놓은 숫자
turn = True # 차례 설정 tre이면 상근이 false이면 근상이
finsh = False   # 현재 테이블에 올려놓은 숫자 초기화 여부
while sanggeun and geunsang:    # 상근이나 근상이 리스트가 None이면 탈출
    if finsh:   # 현대 테이블 초기화 여부 확인 후 값 확인
        now=0
        finsh = False
    if turn:    # 상근이 차례
        if now!=0:  # 현재 테이블에 카드기 있는지 확인
            finsh = True    # 비교할 카드가 있으면 초기화 여부 true
            for i in sanggeun:  # 상근이 수가 테이블보다 크면
                if i>now:
                    now = i # 테이블 수 교체
                    sanggeun.remove(i)  # 상근이 리스트에서 낸 수 삭제
                    finsh = False   # 낼 수가 있으므로 초기화 여부 false
                    break
        else:
            now=sanggeun.pop(0)
        turn = False    # 근상이 차례로 설정
    else:   # 근상이 차례 위와 같음
        if now!=0:
            finsh = True
            for i in geunsang:
                if i>now:
                    now = i
                    geunsang.remove(i)
                    finsh = False
                    break
        else:
            now=geunsang.pop(0)
        turn = True # 상근이 차례로 설정
print(len(geunsang))
print(len(sanggeun))

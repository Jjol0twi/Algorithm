import sys
n = int(sys.stdin.readline().strip())                           # 숫자 길이 입력 받기
t = [sys.stdin.readline().strip().split() for _ in range(n)]    # 팀원 리스트 입력 받기
while len(t)!=1:    # 화석이랑 같이 팀원할 한명의 팀원이 남을 때 까지
    a = (int(t[0][1])-1)%(len(t)-1) # 시간 초과를 예상하여 학번-1%남은 사람 수 근데 해당 학번 사람 수 빼고
    b = t[1:(a+1)]  # 뒤로 보낼 사람 리스트
    del t[:a]   # 뒤로 보낼 사람 리스트는 팀원 리스트에서 지우기
    t.extend(b) # 리스트 확장 함수 사용해서 뒤에 붙이기
    del t[:2]   # 짝짝꿍해서 나갈 새내기 없애기
print(t[0][0])  # 화석이랑 같이 할 희생양? 출력

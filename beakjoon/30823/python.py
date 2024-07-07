from sys import stdin
# 문제 규칙을 파악해서 푼 문제
# 앞에서부터 k만큼 뒤로 보내되 (n-k)+₩
n, k = map(int, stdin.readline().strip().split())   # n, k 입력받기
s = list(stdin.readline().strip())  # s list로 받기
rs = s[:(k-1)]  # 앞에서부터 k만큼 rs에 저
del s[:(k-1)]   #
if (n-k)%2==0:
    rs.reverse()
print(''.join([*s,*rs]))

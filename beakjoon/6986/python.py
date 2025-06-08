from sys import stdin
n, k = map(int, stdin.readline().strip().split())
sc = [float(stdin.readline().strip()) for _ in range(n)]
sc.sort()
if k==0:    # 꼭 k가 0일 때 계산처
    print("{:.2f}\n{:.2f}".format(sum(sc)/n + 1e-8,sum(sc)/n + 1e-8))
else:
    scs = sum(sc[k:-k]) # 중복되는 점수의 k부터 뒤에서 k까지
    print("{:.2f}\n{:.2f}".format(scs/(n-(k*2)) + 1e-8,(scs+(sc[k]*k)+(sc[-(k+1)]*k))/n + 1e-8))    # 부동소수점 확인 필수

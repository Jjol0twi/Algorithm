from sys import stdin

def getPrimeList(s, f):
    _result = []
    for i in range(s,f+1):
        if i <= 1:
            continue
        if i <= 3:
            _result.append(i)
            continue
        if i % 2 == 0 or i % 3 == 0:
            continue
        is_prime = True
        e = 5
        while e * e <= i:
            if i % e == 0 or i % (e + 2) == 0:
                is_prime = False
                break
            e += 6
        if is_prime:
            _result.append(i)
    return set(_result)

a, b = map(int, stdin.readline().split())
c, d = map(int, stdin.readline().split())
ytList = getPrimeList(a,b)
yjList = getPrimeList(c,d)
commonPrimes = ytList & yjList
if not commonPrimes:
    print("yj")
elif len(commonPrimes) % 2 == 1:
    print("yt")
else:
    print("yj")

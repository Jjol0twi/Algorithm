import sys
n = 1000 - int(sys.stdin.readline())
cl = [500, 100, 50, 10, 5, 1]
r = 0
for i in cl:
	r+=n//i
	n%=i
print(r)

import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split()[:6])
y = (a*f-d*c)//(a*e-d*b)
# x = (c-b*y)//a
x = (b*f-e*c)//(d*b-e*a)
# y = (c-a*x)//b
print(int(x), int(y))

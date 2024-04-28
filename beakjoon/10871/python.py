import sys
n, x = list(map(int,sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()[:n]))
for i in range(n):
    if a[i]<x:
        print(a[i], end=" ")

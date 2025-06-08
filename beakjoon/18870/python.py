from sys import stdin
n = int(stdin.readline())
xList = list(map(int, stdin.readline().split()))
xLlist_sort = sorted(set(xList))
xList_dic = {value: index for index, value in enumerate(xLlist_sort)}
result = [xList_dic[i] for i in xList]
print(*result)

import sys
k=int(sys.stdin.readline())
testcase = []
for i in range(k):
    m, n, p = map(int,sys.stdin.readline().split())
    testcase.append([list(map(lambda x: int(x) if x.isdigit() else x, sys.stdin.readline().split())) for j in range(n)])
for i in range(k):
    cs={}
    for j in testcase[i]:
        if j[0] in cs:
            if j[1] in cs[j[0]]:
                if not cs[j[0]][j[1]][1]:
                    cs[j[0]][j[1]] = [cs[j[0]][j[1]][0]+j[2], j[3]] if j[3] else [cs[j[0]][j[1]][0]+20, j[3]]
            else:
                cs[j[0]][j[1]] = [j[2], j[3]] if j[3] else [20, j[3]]
        else:
            cs[j[0]]={}
            cs[j[0]][j[1]] = [j[2], j[3]] if j[3] else [20, j[3]]
    result=[]
    for id, values in cs.items():
        true_count = sum([v[1] for v in values.values()])
        true_score_sum = sum([v[0] for k, v in values.items() if v[1]])
        result.append([id, true_count, true_score_sum])
    result.sort(key=lambda x: (-x[1], x[2]))
    print("Data Set {}:".format(i+1))
    for j in result:
        print(' '.join(map(str,j)))
    print()

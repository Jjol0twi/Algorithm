def fibonacci(n: int):
    if n<1:
        return 0
    if n==1 or n==2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

testNum = int(input())
testCase = []
for i in range(testNum):
    testCase.append(list(map(int, input().split())))
result=[]
for i in range(len(testCase)):
    print("Case #{}: {}".format(i+1,fibonacci(testCase[i][0])%testCase[i][1]))

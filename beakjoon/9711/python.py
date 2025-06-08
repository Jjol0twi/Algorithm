import sys
sys.setrecursionlimit(10**6)
def fibonacci(n: int):
    if n < 1:
        return []
    # fib_list=[1,1]  # 재귀함수 runtime error로 for문으로 교체
    # for i in range(2, n):
    #     fib_list.append(fib_list[-1] + fib_list[-2])
    # return fib_list
    if n == 1 or n==2:
        return [1, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

testNum = int(input())
testCase = []
for i in range(testNum):
    testCase.append(list(map(int, input().split())))
max_fibonacci_index = max(i[0] for i in testCase)
fibonacci_list = fibonacci(max_fibonacci_index)
for i in range(len(testCase)):
    print("Case #{}: {}".format(i+1,fibonacci_list[testCase[i][0]-1]%testCase[i][1]))

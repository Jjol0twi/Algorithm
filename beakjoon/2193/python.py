from sys import stdin
fibonacci_list = []

def fibonacci(i):
    for j in range(i):
        if j == 0 or j == 1:
            _v = 1
        #     return 1
        else:
            _v = fibonacci_list[j-1] + fibonacci_list[j-2]
        #     v = fibonacci(i-1) + fibonacci(i-2)
        #     return v
        fibonacci_list.append(_v)

n = int(stdin.readline())
# print(fibonacci(n))
fibonacci(n)
print(fibonacci_list[n-1])

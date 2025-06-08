# 실퍠
import sys
n, k = list(map(int, sys.stdin.readline().split()))
kit = list(map(int, sys.stdin.readline().split()[:n]))
kit = [i-k for i in kit]
def permutations(arr):
    _arr = arr
    output = []
    results = []
    def _perm_visited(arr, output, depth):
        if (depth == 3):
            results.append(output[:])
            return
        for i in range(len(arr)):
            new_output = output + [arr[i]]
            _perm_visited(arr, new_output, depth + 1)
    _perm_visited(_arr, output, 0)
    return results
print(permutations(kit))

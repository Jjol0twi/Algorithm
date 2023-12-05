import re

N = input()
answer = 0
for i in range(2023, int(N) + 1):
    b = re.search('2023', str(i))
    print(b)
print(answer)

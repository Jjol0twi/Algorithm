from sys import stdin
r, c = map(int, stdin.readline().split())
cd = [str(stdin.readline().strip()[:c]) for _ in range(r)]
er, ec = map(int, stdin.readline().split())
er, ec = er - 1, ec - 1
for i in range(r):
    cd[i] += cd[i][::-1]
cd = cd + cd[::-1]
cd[er] = cd[er][:ec] + ('.' if cd[er][ec] == '#' else '#') + cd[er][ec+1:]
print('\n'.join(cd))

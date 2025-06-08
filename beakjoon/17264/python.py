from sys import stdin
n, p = map(int, stdin.readline().strip().split())
w, l, g = map(int, stdin.readline().strip().split())
win_player = [name for name, flag in (stdin.readline().strip().split() for _ in range(p)) if flag == 'W']
record = [stdin.readline().strip() for _ in range(n)]
game_score = 0

for i in record:
    if i in win_player:
        game_score += w
    else:
        game_score -= l
        if game_score<0:
            game_score = 0
    if game_score>=g:
        print("I AM NOT IRONMAN!!")
        exit()

print("I AM IRONMAN!!")

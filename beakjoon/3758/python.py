# from sys import stdin
# from itertools import groupby

# testdata_num = int(stdin.readline())
# result = []
# for _ in range(testdata_num):
#     testdata_info = list(map(int, stdin.readline().split()))
#     testdata = [list(map(int, stdin.readline().split())) for _ in range(testdata_info[3])]
#     testdata_result = [[i+1,0,0,0] for i in range(testdata_info[0])]
#     testdata_sorted = [
#         max(group, key=lambda x: x[2])
#         for _, group in groupby(
#             sorted(testdata, key=lambda x: (x[0], x[1])),
#             key=lambda x: (x[0], x[1])
#         )
#     ]
#     for i in range(len(testdata_sorted)):
#         testdata_result[(testdata_sorted[i][0]-1)][1]+=testdata_sorted[i][2]
#         testdata_result[(testdata_sorted[i][0]-1)][2]+=1
#         testdata_result[(testdata_sorted[i][0]-1)][3]=i
#     testdata_result.sort(key=lambda x: (-x[1], x[2], x[3]))
#     for i in testdata_result:
#         if i[0]==testdata_info[2]:
#             result.append(testdata_result.index(i)+1)
# print(*result, sep="\n")
from sys import stdin
from collections import defaultdict

def find_team_rank():
    n_teams, n_problems, my_team, n_logs = map(int, stdin.readline().split())
    testcase_score = defaultdict(int)
    team_stats = defaultdict(lambda: [0, 0])
    for time in range(n_logs):
        team_id, prob_id, score = map(int, stdin.readline().split())
        testcase_score[(team_id, prob_id)] = max(testcase_score[(team_id, prob_id)], score)
        team_stats[team_id][0] += 1
        team_stats[team_id][1] = time
    rankings = []
    for team_id in range(1, n_teams + 1):
        total_score = sum(testcase_score[(team_id, prob_id)]
                         for prob_id in range(1, n_problems + 1))
        submissions, last_time = team_stats[team_id]
        rankings.append((-total_score, submissions, last_time, team_id))
    rankings.sort()
    for rank, (_, _, _, team_id) in enumerate(rankings, 1):
        if team_id == my_team:
            return rank
test_cases = int(stdin.readline())
results = [find_team_rank() for _ in range(test_cases)]
print(*results, sep='\n')

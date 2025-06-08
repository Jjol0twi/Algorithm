#     whine = ("aya", "ye", "woo", "ma")
#     for i in range(len(babbling)):
#         for j in whine:
#             startindex = 0
#             for x in range(babbling[i].count(j)):
#                 index = babbling[i].find(j) + len(j)
#                 if startindex == index:
#                     break
#                 startindex = index
#                 babbling[i] = babbling[i].replace(j, "", 1)
#     return sum(1 for i in babbling if not i)
def solution(babbling):
    whine = ("aya", "ye", "woo", "ma")
    for i in range(len(babbling)):
        stack = 0
        while stack != len(whine):
            for j in whine:
                stack += (1 if babbling[i].find(j) == 1 else 0)
                index = babbling[i].find(j)
                if index == 0 or index + len(j) == len(babbling[i]):
                    babbling[i] = babbling[i][:index] + babbling[i][index + len(j):]
                else:
                    continue
    return sum(1 for i in babbling if not i)


# replace를 할 경우에 중간에 있는 단어를 삭제하기에 yayae같은 예제들에서 빠진다.
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
wow = solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
print(wow)

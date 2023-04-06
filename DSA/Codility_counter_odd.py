from collections import Counter


def Solution(A):
    # name = list(Counter(A).keys())
    # count = list(Counter(A).values())
    # for i in range(len(count)):
    #     if count[i] == 1:
    #         return name[i]
    s = set()
    for i in A:
        s.add(i) if i not in s else s.remove(i)
    return list(s)[0]


A = [9, 3, 9, 3, 9, 5, 9, 7, 7]
print(Solution(A))

# print(Solution(A))

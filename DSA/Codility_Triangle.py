from itertools import combinations


def solution(A):
    combi_obj = combinations(A, 3)
    result = [
        x
        for x in list(combi_obj)
        if (x[0] + x[1]) > x[2] and (x[0] + x[2]) > x[1] and (x[1] + x[2]) > x[0]
    ]
    if len(result) > 0:
        return 1
    return 0

    # A.sort()
    # result = 0
    # for i in range(len(A)-2):
    #     if (A[i] + A[i+1]) > A[i+2]:
    #         return 1
    # return 0


A = [10, 2, 5, 1, 8, 20]


B = [10, 50, 5, 1]
C = [1, 1, 1, 1, 5, 5, 5]
print(solution(B))

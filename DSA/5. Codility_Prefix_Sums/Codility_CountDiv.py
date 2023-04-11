import math


def solution(A, B, K):  # O(1)
    low = math.ceil(A / K)
    high = math.floor(B / K)
    return high - low + 1


print(solution(6, 11, 2))

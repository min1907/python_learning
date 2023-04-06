def solution(A):  # Comlexity O(N*N)
    result = 0
    N = len(A)
    for P in range(N):
        if A[P] == 0:
            for Q in range(P + 1, N):
                if A[Q] == 1:
                    result += 1
                    if result > 1000000000:
                        return -1
    return result


# print(solution(A))
# from itertools import combinations
# result = [x for x in list(combinations(A,2)) if x[0] == 0 and x[1] == 1]
# print(len(result))

# Solution 2
from itertools import combinations


def solution2(A):  # O(N*N)
    result = [x for x in list(combinations(A, 2)) if x[0] == 0 and x[1] == 1]
    if result > 1000000000:
        return -1
    return len(result)


# Solution 3
def solution3(A):  # O(N)
    count = 0
    multiply = 0
    for i in A:
        if i == 0:
            multiply += 1
        if i == 1:
            count += multiply
    if count > 1000000000:
        return -1
    return count


A = [0, 1, 0, 1, 1]
B = [1, 0, 0, 1, 1]
print(solution3(A))
print(solution3(B))

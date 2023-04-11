import sys


def sum_diff(A, p):
    sum1 = 0
    n = len(A)
    for i in range(p):
        sum1 += A[i]

    sum2 = 0
    for i in range(p, n):
        sum2 += A[i]
    return abs(sum1 - sum2)


def solution(A):  # O(N*N)
    # Implement your solution here
    n = len(A)
    result = sys.maxsize
    for i in range(1, n):
        result = min(result, sum_diff(A, i))
    return result


A = [0, 1, 2, 3, 4, 5]
# print(solution(A))


def solution2(A):  # O(N*N)
    leftsum = 0
    result = sys.maxsize
    for i in A:
        leftsum += i
        result = min(abs(2 * leftsum - sum(A)), result)
    return result


# print(solution2(A))


from itertools import accumulate


def solution3(A):  # O(N) --> best
    s = sum(A)
    l = list(accumulate(A[:-1]))
    return min([abs(2 * x - s) for x in l])

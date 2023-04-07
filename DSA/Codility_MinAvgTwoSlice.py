import sys


def solution(A):
    N = len(A)
    min_avg = sys.maxsize
    pos = A[0]
    for i in range(N):
        for j in range(i + 1, N):
            if average(A, i, j) <= min_avg:
                min_avg = average(A, i, j)
                pos = i
    return pos


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def average(A, x, y):  # P=prefix_sums(A)
    P = prefix_sums(A)
    return (P[y + 1] - P[x]) / (y - x + 1)


A = [4, 2, 2, 5, 1, 5, 8]

# min_value = 100
# for i in range(len(A)):
#     for j in range(i+1, len(A)):
#         #print(i,j,average(A,i,j))
#         if average(A,i,j) <= min_value:
#             min_value = average(A,i,j)
#             print(min_value, A[i])

# print(solution(A))


######
## OPTIMIZE SOLUTION
"""
The key to solve this task is these two patterns:
    (1) There must be some slices, with length of two or three, having the minimal average value among all the slices.
    (2) And all the longer slices with minimal average are built up with these 2-element and/or 3-element small slices.

Firstly we will prove the statement (1). In all the following discussion, we assume the slices have two or more elements.
In every array, there must be at lease one slice, to say S, having the Minimal Average (MA). And PLEASE PAY ATTENTION,
the following proof is done with the S, which HAS the global minimal average.

    a. If the length of S is two or three, it follows our conclusion.

    b. If the length of S is odd, we could divide it into a 3-element sub-slice and some 2-element sub-slice.
        For example, for the slice [1, 2, 3, 4, 5], we could get a 3-element sub-slice [1, 2, 3] and a 2-element sub-slice [4, 5].
        Or differently we could get [1, 2] and [3, 4, 5]. But the split does not matter in the following prove.
            . If the sub-slices have different averages, some of them will have smaller average than MA.
            But it conflicts with the condition that, the MA is known as the global minimal average for all slices.
            By this contradictory, it’s proved that all the sub-slices MUST have the same average.

            . If all the sub-slices have the same average, the average of them must be MA. So all these sub-slices have overall minimal average and length of two or three.

    c. If the length of S is even, we could divide it into some 2-element sub-slice.
            For the slice [1, 2, 3, 4], the only possible split is [1, 2] and [3, 4]. Then, similar with the previous case, all these 2-element sub-slices have the global minimal average.

And in the construction in step b, we have already proven the statement (2).
"""


def solution2(A):
    min_avg_value = (A[0] + A[1]) / 2.0  # The mininal average
    min_avg_pos = 0  # The begin position of the first
    # slice with mininal average
    for index in range(0, len(A) - 2):
        # Try the next 2-element slice
        if (A[index] + A[index + 1]) / 2.0 < min_avg_value:
            min_avg_value = (A[index] + A[index + 1]) / 2.0
            min_avg_pos = index
        # Try the next 3-element slice
        if (A[index] + A[index + 1] + A[index + 2]) / 3.0 < min_avg_value:
            min_avg_value = (A[index] + A[index + 1] + A[index + 2]) / 3.0
            min_avg_pos = index
    # Try the last 2-element slice
    if (A[-1] + A[-2]) / 2.0 < min_avg_value:
        min_avg_value = (A[-1] + A[-2]) / 2.0
        min_avg_pos = len(A) - 2
    return min_avg_pos


print(solution2(A))

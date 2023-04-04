# We consider problems in which a result comprises a sequence of steps or choices that have
# to be made to achieve the optimal solution. Greedy programming is a method by which
# a solution is determined based on making the locally optimal choice at any given moment.
# In other words, we choose the best decision from the viewpoint of the current stage of the
# solution.
# Depending on the problem, the greedy method of solving a task may or may not be
# the best approach. If it is not the best approach, then it often returns a result which is
# approximately correct but suboptimal. In such cases dynamic programming or brute-force
# can be the optimal approach. On the other hand, if it works correctly, its running time is
# usually faster than those of dynamic programming or brute-force

# A la list menh gia tien tu nho den lon, k la so tien can quy doi
# A = [1,2,3,4,5]; k=11
# Thuat toan Greedy se di tu tien menh gia lon nhat va giam dan
def greedyCoinChanging(A, k):
    n = len(A)
    result = (
        []
    )  # result su dung de luu ket qua la list cac cap gia tri: (menh gia, so luong to tien)
    for i in range(n - 1, -1, -1):
        if A[i] <= k:
            result += [(A[i], k // A[i])]
            k %= A[i]
    return result


A = [1, 3, 4]
# print(greedyCoinChanging(A, 6)) # result: 4,1,1 but actually it's not optimal because we still have 2 coins which is 3,3


# Canoeist problem
from collections import deque

# Solution A
def greedyCanoeistA(W, k):
    N = len(W)
    light = deque()
    heavy = deque()
    for i in range(N - 1):

        if W[i] + W[-1] <= k:
            light.append(W[i])
        else:
            heavy.append(W[i])
    heavy.append(W[-1])
    canoes = 0
    while light or heavy:
        if len(light) > 0:
            light.pop()
        heavy.pop()
        canoes += 1
        if not heavy and light:
            heavy.append(light.pop())
        while len(heavy) > 1 and heavy[-1] + heavy[0] <= k:
            light.append(heavy.popleft())

    return canoes


# Solution B:  The heaviest canoeist is seated with the lightest, as long as their weight
# is less than or equal to k. If not, the heaviest canoeist is seated alone in the canoe
def greedyCanoeistB(W, k):
    canoes = 0
    j = 0
    i = len(W) - 1
    while i >= j:
        if W[i] + W[j] <= k:
            j += 1
        canoes += 1
        i -= 1
    return canoes


W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31, 50]
k = 55
print(greedyCanoeistA(W, k))
print(greedyCanoeistB(W, k))

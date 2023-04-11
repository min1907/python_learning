# Trap: multiplying two negatives makes a positive number.
def solution(A):  # O(N*log(N))
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])


A = [-3, 1, 2, -2, 5, 6]

# print(solution(A))

# B=sorted(A) #A.sort() will replace A with new sorted(A, reverse = False)
# print(B)


# solution2 still same notice
# Trap: multiplying two negatives makes a positive number.


def solution2(A):
    maxes = [
        float("-inf"),
        float("-inf"),
        float("-inf"),
    ]  # float('-inf') == integer.MIN_VALUE
    mins = [
        float("inf"),
        float("inf"),
        float("inf"),
    ]  # float('inf') == integer.MAX_VALUE;
    # O(N)
    for a in A:
        updateMaxes(a, maxes)
        updateMins(a, mins)
    print(maxes, mins)
    obvious = maxes[0] * maxes[1] * maxes[2]
    print(obvious)
    twoBigNegs = mins[0] * mins[1] * maxes[2]
    print(twoBigNegs)
    return max(obvious, twoBigNegs)


def updateMaxes(a, maxes):
    # Found new max
    if a >= maxes[2]:
        maxes[0] = maxes[1]
        maxes[1] = maxes[2]
        maxes[2] = a
    elif a >= maxes[1]:
        maxes[0] = maxes[1]
        maxes[1] = a
    elif a >= maxes[0]:
        maxes[0] = a


def updateMins(a, mins):
    if a <= mins[0]:
        mins[1] = mins[0]
        mins[0] = a
    elif a < mins[1]:
        mins[1] = a


A = [-3, 1, 2, 2, -5, -6]
print(solution2(A))

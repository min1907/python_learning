def F_upto_A(L):
    """
    Fibonacci sequence up to the
    length of A (including starting and destination position)
    """
    F = []
    F.append(0)
    F.append(1)
    while F[-1] <= L:
        F.append(F[-1] + F[-2])
    return F[1:-1]  # remove F[0] = 0


def solution(A):  # using dynamic programming method
    # add starting position of A
    A.insert(0, 1)
    # add destination position of A
    A.append(1)  # A = [1,0,0,0,1,1,0,1,0,0,0,0,1] # A[0] -> A[12]
    n = len(A)  # 13
    # store available Fibonacci jumps
    F = F_upto_A(n)  # F = [1,1,2,3,5,8,13]
    # S mapping A in position and
    # store the minimum step count to each "1" postion
    S = [n] * n  # [13,13,13,13,13,13,13,13,13,13,13,13,13]
    S[0] = 0  # [0,13,13,13,13,13,13,13,13,13,13,13,13]
    for i in range(1, n):
        # check if the postion is 1 in A
        # print(f"i = {i}")
        if A[i] == 1:
            # loop the Fibonacci sequence F = [1,1,2,3,5,8,13]
            for x in F:
                # previous position
                prev = i - x
                if prev >= 0:
                    """
                    the minimum step count of previous position
                    plus
                    one more step to the existing position;
                    if less than the step count of the existing position;
                    update the step count of the existing position
                    """
                    if S[prev] + 1 < S[i]:
                        S[i] = S[prev] + 1
                    # print(f"i = {i},x = {x},S = {S}")
                else:  # prev < 0 or i < x : can not find any number to reach that position
                    break
    """
    return the last position of S,
    if S[-1] == n means destination can not be reached
    S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 3]
    """
    return S[-1] if S[-1] < n else -1


A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A))

# i = 1
# i = 2
# i = 3
# i = 4
# i = 4,x = 1,S = [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# i = 4,x = 1,S = [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# i = 4,x = 2,S = [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# i = 4,x = 3,S = [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# i = 5
# i = 5,x = 1,S = [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# i = 5,x = 1,S = [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# i = 5,x = 2,S = [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# i = 5,x = 3,S = [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# i = 5,x = 5,S = [0, 13, 13, 13, 13, 1, 13, 13, 13, 13, 13, 13, 13]
# i = 6
# i = 7
# i = 7,x = 1,S = [0, 13, 13, 13, 13, 1, 13, 13, 13, 13, 13, 13, 13]
# i = 7,x = 1,S = [0, 13, 13, 13, 13, 1, 13, 13, 13, 13, 13, 13, 13]
# i = 7,x = 2,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 13]
# i = 7,x = 3,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 13]
# i = 7,x = 5,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 13]
# i = 8
# i = 9
# i = 10
# i = 11
# i = 12
# i = 12,x = 1,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 13]
# i = 12,x = 1,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 13]
# i = 12,x = 2,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 13]
# i = 12,x = 3,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 13]
# i = 12,x = 5,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 3]
# i = 12,x = 8,S = [0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 3]
# 3

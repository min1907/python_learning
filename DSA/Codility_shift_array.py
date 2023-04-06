from collections import deque


def Solution(A, K):
    myarray = deque(A)
    myarray.rotate(K)
    return list(myarray)


A = [1, 2, 3, 4, 5, 6]
Solution(A, 2)

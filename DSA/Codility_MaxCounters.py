def solution(N, A):  # Complexity O(N*M)
    arrN = [0] * N
    for i in range(len(A)):
        # print(arrN)
        if 1 <= A[i] <= N:
            arrN[A[i] - 1] += 1
        if A[i] == N + 1:
            m = max(arrN)
            for j in range(len(arrN)):
                arrN[j] = m
    return arrN


A = [3, 4, 4, 6, 1, 4, 4]
N = 5

print(solution(N, A))

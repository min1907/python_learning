from collections import Counter


def check(M, N):
    if Counter(M) == Counter(N):
        return True
    return False


def solution(A, B):
    count = 0
    # result = []
    for i in range(len(A)):
        for j in range(i, len(A)):
            if check(A[i : j + 1], B[i : j + 1]) == True:
                count += 1
                # result.append((A[i:j+1],B[i:j+1]))
    return count


A = "dBacaAA"
B = "caBdaaA"
# return 5
print(solution(A, B))

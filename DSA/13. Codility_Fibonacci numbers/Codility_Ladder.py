def solution(A, B):  # O(L**2)

    N = max(A)
    Fib = [0] * (N + 2)
    Fib[0] = 0
    Fib[1] = 1
    for i in range(2, N + 2):
        Fib[i] = Fib[i - 1] + Fib[i - 2]
    # print(Fib)
    # Fib = [0, 1, 1, 2, 3, 5, 8]

    result = []
    len_A = len(A)
    for i in range(len_A):
        result.append(Fib[A[i] + 1] % (2 ** B[i]))
    return result


# A = [4,4,5,5,1]
# B = [3,2,4,3,1]
A = [4]
B = [1]
print(solution(A, B))
# print(count_num_ways(A))

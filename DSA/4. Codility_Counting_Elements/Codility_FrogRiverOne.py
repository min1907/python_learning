def solution(X, A):
    check = set()
    for i in range(len(A)):
        # print(i,A[i])
        if A[i] not in check and A[i] <= X:
            check.add(A[i])
            # print(list(check), len(list(check)))

            if len(list(check)) == X:
                return i
    return False


A = [1, 3, 1, 4, 2, 3, 5, 4]
# print(solution(4,A))


def solution2(X, A):  # O(N)
    dict_tmp = {}
    i = 0
    while i < len(A):
        dict_tmp[A[i]] = i
        print(dict_tmp)
        if len(dict_tmp) == X:
            return i
        i += 1
    return -1


A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution2(4, A))

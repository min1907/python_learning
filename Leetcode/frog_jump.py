def frog_jump(X, A) -> int:
    i = 0
    dict_tmp = {}
    while i < len(A):
        dict_tmp[A[i]] = i
        print(dict_tmp)
        if len(dict_tmp) == X:
            return i
        i += 1
    return -1


A = [1, 3, 1, 4, 2, 3, 4, 4, 5]
X = 4

print(frog_jump(X, A))

def solution(A):  # 83% Codility
    n = len(A)
    if n == max(A):
        return 1
    else:
        return 0


A = [1, 2, 4, 5]
print(solution(A))


from itertools import permutations

# perm = permutations([1, 2, 3])
# for i in list(perm):
#     print (type(i))

# print(list(range(1,5)))


def solution2(A):
    list_check = list(range(1, len(A) + 1))
    perm = permutations(list_check)
    if tuple(A) in list(perm):
        return 1
    return 0


print(solution2(A))

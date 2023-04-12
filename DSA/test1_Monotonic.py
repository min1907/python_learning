# def check_ascending(A,P,Q):
#     if P == Q:
#         return True
#     else: #P != Q
#         if len(A[P:Q+1]) != len(set(A[P:Q+1])): # there are duplicated element in slice
#             return False
#         if A[P:Q+1] == sorted(A[P:Q+1]):
#             return True
#         else:
#             return False


def check_ascending(A, P, Q):
    if P == Q:
        return True
    else:  # P != Q
        if len(A[P : Q + 1]) == len(set(A[P : Q + 1])) and A[P : Q + 1] == sorted(
            A[P : Q + 1]
        ):
            return True
        else:
            return False


def solution(A):
    max_size = 1  # we always have an ascending slice with size 1
    n = len(A)
    begin_slice = 0

    for P in range(n):
        for Q in range(P, n):
            # print(i,j)
            if check_ascending(A, P, Q) == True:
                # print("True",i,j)
                size = Q - P + 1
                if size > max_size:
                    max_size = size
                    begin_slice = P
                    # print(f"max_size = {max_size}, element = {element}")
    return begin_slice


A = [2, 2, 2, 2, 1, 2, -1, 2, 1, 3]
print(solution(A))
B = [30, 20, 10]
print(solution(B))
C = [2, -2, -1, 0, -3, 4, 6, 8, 3, 1]
# print(solution(C))

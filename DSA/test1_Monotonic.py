def MaxDistanceMonotinic(A):
    N = len(A)
    result = 0
    for P in range(N - 1):
        for Q in range(P + 1, N):
            # print(A[P], A[Q])
            # print("==============")
            if A[P] <= A[Q]:
                result = max(result, Q - P)
                print(f"{A[P]}, {A[Q]}, {result}")
                print("++++ end loop Q ++++")
    return result


A = [2, 2, 2, 2, 1, 2, -1, 2, 1, 3]
print(MaxDistanceMonotinic(A))

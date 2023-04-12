def solution(A):  # 100% O(N) or O(N*logN)
    B = set()
    for element in A:
        if not abs(element) in B:
            # print(abs(element))
            B.add(abs(element))
            # print(B)
    return len(B)


A = [-5, -3, -1, 0, 3, 6]
print(solution(A))
# should return 5 as 0,1,3,5,6

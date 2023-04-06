def solution(A):
    # Implement your solution here
    m = max(A)
    if m < 1:
        return 1

    A = set(A)
    B = set(range(1, m + 1))
    D = B - A
    if len(D) == 0:
        return m + 1
    else:
        return min(D)


A = [1, 3, 6, 4, 1, 2, 0, -1, 100, 90, 8]
print(solution(A))

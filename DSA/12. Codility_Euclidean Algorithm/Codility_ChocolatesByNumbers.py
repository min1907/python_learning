def solution(N, M):  # O(N+M) --> 62%
    if N == 1:
        return 1
    result = 1
    remander = (0 + M) % N

    while remander != 0:
        remander = (remander + M) % N
        result += 1
    return result


print(solution(20, 4))

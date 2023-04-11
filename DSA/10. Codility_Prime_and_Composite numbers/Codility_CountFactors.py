def solution(N):
    candidate = 1
    result = 0
    while candidate * candidate < N:
        # N has 2 factors : candidate and N//candidate
        if N % candidate == 0:
            result += 2
        candidate += 1
    # if N is square of a value
    if candidate * candidate == N:
        result += 1
    return result


print(solution(16))

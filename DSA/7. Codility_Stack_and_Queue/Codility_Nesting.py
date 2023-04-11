def solution(S):
    parentheses = 0
    for i in S:
        if i == "(":
            parentheses += 1
        else:
            parentheses -= 1
            if parentheses < 0:
                return 0

    if parentheses == 0:
        return 1
    else:
        return 0


S1 = "(()("
S2 = "(())"
print(solution(S1))
print(solution(S2))

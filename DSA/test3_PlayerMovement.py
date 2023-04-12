from collections import deque


def solution(A):
    result = 0
    S = deque(A)
    N = len(S)
    for i in range(N):
        print(f"element = {S[i]}")
        if i == 0 and (S[i] == "<" or S[i] == "^" or S[i] == "v"):
            # print("if1")
            # S[i] = "empty"
            result += 1
            # print(result)
        elif i == N - 1 and S[i] == ">":
            # print("if2")
            result += 1
            # print(result)
        elif S[i] == "^" or S[i] == "v":
            # print("if3")
            S[i] = "empty"
            result += 1
            # print(result)
        else:  # i>0 and (S[i] == "<" or S[i] == ">")
            # print("if4")
            if S[i - 1] == "empty" and S[i] == "<":
                result += 1
            # print(result)
    return result


S1 = "><^v"
# print(solution(S1))

S2 = "<<^<v>>"
# print(solution(S2))

S3 = "><><"
print(solution(S3))

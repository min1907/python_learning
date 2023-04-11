def solution(S, P, Q):  # O(N*M)
    translations = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4,
    }
    list_change = []
    for character in S:
        list_change.append(int(str(translations.get(character))))
    print(S, list_change)
    # print(min(list_change[0:1]))
    M = len(P)
    # result = [0] * M
    result = []
    for i in range(M):
        # print(P[i], Q[i])
        if P[i] <= Q[i]:
            result.append(find_min(list_change, P[i], Q[i]))

    return result


def find_min(A, m, n):
    if m == n:
        return A[m]
    result = A[m]
    for k in range(m, n + 1):
        result = min(result, A[k])
    return result


S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))
# print(find_min([2, 1, 3, 2, 2, 4, 1],5,5))

# my_dict = {
#     "A": 1,
#     "C": 2,
#     "G": 3,
#     "T": 4,
# }
# re_text = []
# for i in S:
#     re_text.append(int(str(my_dict.get(i))))
#     re_text_new = int(re_text)
# print(re_text)

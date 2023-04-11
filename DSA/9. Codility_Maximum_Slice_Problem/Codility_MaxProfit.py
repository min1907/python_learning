def solution(A):  # O(N*N)
    max_profit = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            max_profit = max(max_profit, A[j] - A[i])
    return max_profit


A = [23171, 21011, 21123, 21366, 21013, 21367]
B = [23171, 21011]
# print(solution(A))


def solution2(A):  # O(N)
    # we travel from last element to the first one
    days = len(A)
    if days < 2:  # number of days is 0 or 1, there is no time to get profit
        return 0
    max_profit = 0
    max_price_from_here = A[days - 1]
    for day in range(days - 2, -1, -1):
        max_profit = max(max_profit, max_price_from_here - A[day])
        max_price_from_here = max(A[day], max_price_from_here)
    return max_profit


print(solution2(B))

"""
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

co 11 cap duong tron intersection

0th and 1st
0th and 2nd
0th and 4th
1st and 2nd
1st and 3rd
1st and 4th
1st and 5th
2nd and 3rd
2nd and 4th
3rd and 4th
4th and 5th
"""


def solution(A):
    N = len(A)
    result = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if (j - i) <= max(A[i], A[j]):
                result += 1
                if result >= 10000000:
                    return -1
    return result


A = [1, 5, 2, 1, 4, 0]
print(solution(A))

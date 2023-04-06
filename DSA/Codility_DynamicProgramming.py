"""
Dynamic programming is a method by which a solution is determined based on solving
successively similar but smaller problems. This technique is used in algorithmic tasks in
which the solution of a bigger problem is relatively easy to find, if we have solutions for its
sub-problems.
"""
# Come back to coin changing problem
import sys


def dynamic_coin_changing(
    C, k
):  # Time complexity and Space complexity O(n.k) (can 1 mang chua n.k de luu ket qua)
    n = len(C)
    # create 2-D array with all zeros
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0] = [0] + [sys.maxsize] * k
    for i in range(1, n + 1):
        for j in range(C[i - 1]):
            dp[i][j] = dp[i - 1][j]
        for j in range(C[i - 1], k + 1):
            dp[i][j] = min(dp[i][j - C[i - 1]] + 1, dp[i - 1][j])
    return dp[n]


A = [1, 3, 4]
# print(dynamic_coin_changing(A,6))


def dynamic_coin_changing2(
    C, k
):  # Time complexity O(n.k), Space complexity O(k) (can 1 mang chua k phan tu de luu ket qua)
    n = len(C)
    dp = [0] + [sys.maxsize] * k
    for i in range(1, n + 1):
        for j in range(C[i - 1], k + 1):
            dp[j] = min(dp[j - C[i - 1]] + 1, dp[j])
    return dp


# print(dynamic_coin_changing2(A,6))

"""
Problem:
A small frog wants to get from position 0 to k (1 <= k <= 10 000). The frog can
jump over any one of n fixed distances s0, s1, . . . , s(n-1) (1 <= s(i) <= k). The goal is to count the
number of different ways in which the frog can jump to position k. To avoid overflow, it is
sufficient to return the result modulo q, where q is a given number.
We assume that two patterns of jumps are different if, in one pattern, the frog visits
a position which is not visited in the other pattern.

Solution O(n · k): The task can be solved by using dynamic programming. Let’s create an
array dp consisting of k elements, such that dp[j] will be the number of ways in which the
frog can jump to position j.
We update consecutive cells of array dp. There is exactly one way for the frog to jump to
position 0, so dp[0] = 1. Next, consider some position j > 0.
The number of ways in which the frog can jump to position j with a final jump of s(i) is
dp[j-s(i)]. Thus, the number of ways in which the frog can get to position j is increased by
the number of ways of getting to position j-s(i), for every jump s(i)

More precisely, dp[j] is increased by the value of dp[j-si] (for all s(i) <= j) modulo q
"""

# Solution time complexity O(n.k), space complexity O(k)
def frog(S, k, q):
    n = len(S)
    dp = [1] + [0] * k
    for j in range(1, k + 1):
        for i in range(n):
            if S[i] <= j:
                dp[j] = (dp[i] + dp[j - S[i]]) % q
        return dp[k]


S = [1, 2, 3, 4, 5, 6, 8, 9, 10, 13]
k = 18
q = 3
# print(frog(S, k, q))


###########

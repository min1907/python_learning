# https://codility.com/demo/take-sample-test/str_symmetry_point
"""
Write a function:

def solution(S)

that, given a string S, returns the index (counting from 0) of a character
such that the part of the string to the left of that character is a reversal of the part of the string to its right.
The function should return -1 if no such index exists.

Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

For example, given a string:

"racecar"

the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", and the one to the right is "car".

Given a string:

"x"

the function should return 0, because both substrings are empty.
Write an efficient algorithm for the following assumptions:
the length of string S is within the range [0..2,000,000].

"""


def solution(S):  # 100%
    N = len(S)
    # print(list(reversed(S)) == list(S))
    if N % 2 == 0:
        return -1
    if list(reversed(S)) == list(S):
        return N // 2
    else:
        return -1


# def solution(S):
#     # Symetric point is possible, when and only when len(S) is odd
#     N = len(S)
#     if N % 2 == 0:#odd number
#         return -1
#     # With the odd length string, the only possible symetric point is the middle point
#     mid = N // 2
#     begin,end = 0,N-1
#     while begin < mid:
#         if S[begin] != S[end]:
#             return -1
#         begin += 1
#         end -= 1
#     return mid


S = "x"
print(solution(S))

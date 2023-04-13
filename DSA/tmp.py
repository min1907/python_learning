# S = "test 5 a0A pass007 ?xy1"
# print(list(S.split()))

# word = '?xy1'
# num_of_letters = 0
# num_of_digits = 0
# num_of_others = 0
# for letter in word:
#     if letter.isalpha():
#         num_of_letters += 1
#     elif letter.isdigit():
#         num_of_digits += 1
#     else:
#         num_of_others += 1

# print(num_of_letters, num_of_digits, num_of_others)

# '''
# - it has to contain only alphanumerical characters (a-z, A-Z, 0-9);
# - there should be an even number of letters;
# - there should be an odd number of digits.
# '''

# A='12B'
# print(int(A[:-1]) - 1)
# # print(ord(A[-1]) - ord("A"))
from collections import deque

S = "racecar"
# de_S = deque(S)
# print(de_S)
# # de_S.reverse()

# B = list(reversed(de_S))
# print(B)
print(list(reversed(S)))

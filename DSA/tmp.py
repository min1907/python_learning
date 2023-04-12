# from math import sqrt

# N = 26
# # Find out all the primes with Sieve of Eratosthenes
# prime_table = [False] * 2 + [True] * (N - 1)
# prime = []
# prime_count = 0
# for element in range(2, int(sqrt(N)) + 1):
#     if prime_table[element] == True:
#         prime.append(element)
#         prime_count += 1
#         multiple = element * element
#         while multiple <= N:
#             prime_table[multiple] = False
#             multiple += element
# for element in range(int(sqrt(N)) + 1, N + 1):
#     if prime_table[element] == True:
#         prime.append(element)
#         prime_count += 1

# print(prime)

# nails = [(4, 2), (0, 4), (1, 6), (2, 7), (3, 10)]
# print(nails[2][0])

# A = [1,4,5,8]
# B = [4,5,9,10]
# C = list(zip(A,B))
# C.sort()
# print(C)

# A = [3,4,5,5,2]
# print(len(A[0:4]))
# print(len(set(A[0:4])))
# print(A[3:4])
# print(set(A[3:4]))

# A = [2,2,2,2,1,2,-1,2,1,3]

# print(A[5:7])
# print(sorted(A[5:7]))

# def check_ascending(A,i,j):
#     if i == j:
#         return True
#     else: #i != j
#         if len(A[i:j+1]) != len(set(A[i:j+1])):
#             return False
#         if A[i:j+1] == sorted(A[i:j+1]):
#             return True
#         else:
#             return False

# print(check_ascending(A,5,7))


from collections import deque

S = "><^v^"
queue = deque(S)
print(queue)
result = 0
for i in queue:
    if i == "^":
        result += 1
print(result)

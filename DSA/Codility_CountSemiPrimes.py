# Dung Sieve of Eratothense tim tat ca so nguyen to

# def sieve(n):
#     sieve = [True] * (n+1)
#     sieve[0] = False
#     sieve[1] = False
#     i = 2
#     while (i * i < n):
#         if sieve[i]:
#             k = i * i
#             while k <= n:
#                 sieve[k] = False
#                 k += i
#         i += 1
#     return sieve

# print(sieve(20))


def solution(N, P, Q):
    # Find out all the primes with Sieve of Eratosthenes
    sieve = [0] * 2 + [1] * (N - 1)
    element = 2
    while element * element < N:
        if sieve[element]:
            multiply = element * element
            while multiply <= N:
                sieve[multiply] = 0
                multiply += element
        # print(sieve)
        element += 1

    prime = [i for i in range(len(sieve)) if sieve[i] == 1]
    prime_count = len(prime)
    # print(prime, prime_count)
    # prime = [2, 3, 5, 7, 11, 13, 17, 19, 23] and prime_count = 9

    # Compute the semiprimes information
    semiprime = [0] * (N + 1)
    # Find out all semiprimes
    # semiprimes[index] == 1 --> index is semiprime,
    #                   0 --> index is not semiprime
    for index_former in range(prime_count - 1):
        for index_latter in range(index_former, prime_count):
            # print(prime[index_former],prime[index_latter])
            if prime[index_former] * prime[index_latter] > N:
                # this semiprime value is larger than N, no need to record it
                break
            else:  # prime[index_former] * prime[index_latter] <= N
                semiprime[prime[index_former] * prime[index_latter]] = 1
                # pass
    # print(semiprime)
    # semiprime = [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]

    # below is also prefix_sum methodology

    # Compute the number of semiprimes until each position.
    # semiprime[i] == k means:
    # in the range (0,i] there are k semiprimes.
    for index in range(1, N + 1):
        semiprime[index] += semiprime[index - 1]

    # Now after being converted, semiprime = [0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 7, 8, 8, 8, 9, 10]

    # the number of semiprimes within the range [ P[K], Q[K] ]
    # should be semiprime[Q[K]] - semiprime[P[K]-1] (note that semiprime now is the converted array)
    question_len = len(P)
    result = [0] * question_len
    for index in range(question_len):
        result[index] = semiprime[Q[index]] - semiprime[P[index] - 1]
    return result

    # calculate using prefix_sum methodology  - but the performance evaluated will be low based on colidility


#     len_P = len(P)
#     result = [0] * len_P
#     for index in range(len_P):
#         result[index] = total_sum(prefix_sum(semiprime), P[index], Q[index])
#     return result

# def prefix_sum(A):
#     len_A = len(A)
#     P = [0] * (len_A+1)
#     for index in range(1, len_A+1):
#         P[index] = P[index-1] + A[index-1]
#     return P

# def total_sum(P,x,y):
#     return P[y+1] - P[x]

############################################

N = 26
P = [1, 4, 16]
Q = [26, 10, 20]
print(solution(N, P, Q))

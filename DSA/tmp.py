from math import sqrt

N = 26
# Find out all the primes with Sieve of Eratosthenes
prime_table = [False] * 2 + [True] * (N - 1)
prime = []
prime_count = 0
for element in range(2, int(sqrt(N)) + 1):
    if prime_table[element] == True:
        prime.append(element)
        prime_count += 1
        multiple = element * element
        while multiple <= N:
            prime_table[multiple] = False
            multiple += element
for element in range(int(sqrt(N)) + 1, N + 1):
    if prime_table[element] == True:
        prime.append(element)
        prime_count += 1

print(prime)

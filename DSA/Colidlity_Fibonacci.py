# using recursive enumeration as described by definition is very slow (as below)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Faster solution using dynamic programming to find fibonacci number, Time complexity O(n)
def fibonacciDynamic(n):  # find fib(n)
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def fibonacciDynamic2(n):  # show the whole list of fib[0] -> fib[n]
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


# print(fibonacciDynamic(30))

# Another faster algorithm with time complexity O(logn) using matrix multiplication

# Problem: : For all the given numbers x0, x1, . . . , xn−1, such that 1 <= xi <= m <= 1 000 000,
# check whether they may be presented as the sum of two Fibonacci numbers

# 30 -> 832040, 31-> 1346269 > 1000000
# only 31 Fibonacci numbers are smaller than m

import itertools


def find_sum(s, lst):
    return [x for x in itertools.combinations(lst, r=2) if x[0] + x[1] == s]


def Solution(A, lst):
    result = []
    for x in A:
        if find_sum(x, lst):
            # print(find_sum(x,lst))
            result.append(x)
    return result


A = [1, 2, 3, 4, 34, 85, 1000, 5, 7]
print(Solution(A, fibonacciDynamic2(30)))

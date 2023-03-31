# Use the divide and conquer approach when the same subproblem is not solved multiple times.
# Use the dynamic approach when the result of a subproblem is to be used multiple times in the future.
# Let us understand this with an example. Suppose we are trying to find the Fibonacci series. Then,

# Divide and Conquer approach:
# fib(n)
#     If n < 2, return 1
#     Else , return f(n - 1) + f(n -2)

# Dynamic approach:
# mem = []
# fib(n)
#     If n in mem: return mem[n]
#     else,
#         If n < 2, f = 1
#         else , f = f(n - 1) + f(n -2)
#         mem[n] = f
#         return f

# In a dynamic approach, mem stores the result of each subproblem.


# Divide and Conquer Applications
# # Binary Search
# # Merge Sort
# # Quick Sort
# # Strassen's Matrix multiplication
# # Karatsuba Algorithm

# class divide_and_conquer():
#     def merge_sort(self, array: list):
#     #ref: https://www.programiz.com/dsa/divide-and-conquer

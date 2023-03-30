# using %timeit - ref: https://www.guru99.com/timeit-python-examples.html
# import timeit

# class Demo_recursive:
#     def giaithua(self, num):
#         if num == 0:
#             return 1
#         return num * self.giaithua(num - 1)

#     def fibonacci(self, num):
#         if num == 0:
#             return 0
#         if num == 1:
#             return 1
#         return self.fibonacci(num - 1) + self.fibonacci(num - 2)

# starttime = timeit.default_timer()
# print("The start time is: ",starttime)
# print("...running program...")
# tmp = Demo_recursive()
# array = [*range(35)]
# array_map_fibonacci = map(tmp.fibonacci, array)
# print(list(array_map_fibonacci))
# print("...finished...")
# print("The time difference is :", timeit.default_timer() - starttime)

# using cell magic mode %%timeit

# using %lprun to spot and fix bottlebeck -> code profiling for runtime

# usig %mprun -> code profiling for memory usage

########## FROM DATACAMP ###############
# %timeit
# # Create a list of integers(0-50) using list comprehension
# nums_list_comp = [num for num in range(51)]
# print(nums_list_comp)

# # Create a list of integers (0-50) by unpacking range
# nums_unpack = [*range(51)]
# print(nums_unpack)

# nvo@nvo-VirtualBox:~/DEVOPS/PROGRAMMING/PYTHON/python_learning$ ipython
# Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.11.0 -- An enhanced Interactive Python. Type '?' for help.

# In [1]: %timeit range(51)
# 43.5 ns ± 0.477 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

# In [2]: %timeit [num for num in range(51)]
# 630 ns ± 26 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

# # Create a list using formal name
# formal_list = list()
# print(formal_list)

# # Create a list using the literal syntax
# literal_list = []
# print(literal_list)

# # print out the type of formal_list
# print(type(formal_list))

# # print out the type of literal_list
# print(type(literal_list))

# compare the time
# In [1]: %timeit list()
# 20.8 ns ± 1.72 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

# In [2]: %timeit []
# 11.9 ns ± 1.32 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

# Using cell magic mode (%%timeit) from Ipython
# we will be able to identify using numpy array is faster than list with a for loop to make a *2 for all element, code as below
# a = []
# for i in b:
#     a.append(i * 2)

# b_np = np.array(b)
# a_np = b_np * 2

# using %lprun

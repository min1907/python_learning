from collections import Counter

# import random


def find_distinct_value(A):
    list_count = Counter(A)
    return len(list_count)


# A = random.sample(range(100001),100)
# print(A)
A = [2, 1, 1, 2, 3, 1, 4, 5, 5, 6, 7, 8, 9, 10]
print(find_distinct_value(A))

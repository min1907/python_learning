my_dict = {3: [1, 3], 1: [1], 2: [1, 2], 6: [1, 2, 6, 3]}
print(my_dict[6][2])  # 6

my_list = [1, 1, 3, 2, 2, 4, 1, 5]
# print(my_list)
# print(set(my_list))

my_list_2 = [1, 3, 5, 6, 7]
# print(list(enumerate(my_list_2, 1)))

# count number of element in a list and put in dictionary
A = [1, 5, 2, 2]
numbers = {}
for item in A:
    numbers[item] = numbers.get(item, 0) + 1
# numbers = {1: 1, 5: 1, 2: 2}

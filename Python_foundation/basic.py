# Print the name in list that has 6 characters length
names = ["Jerry", "Kramer", "Elaine", "George", "Newman"]
# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)

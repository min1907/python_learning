names = ["adfh", "adjf", "cksdhfdkjfhs"]
primary_types = [1, 1, 3]
secondary_types = ["alpha", "beta", "gamma"]
# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]
# print(names_type1)

# print(*names_type1[:2], sep='\n')

# Combine 3 lists
names_types = [*zip(names, primary_types, secondary_types)]
# print(*names_types[:2], sep='\n')

# Combine 3 items from names and 2 items from primary_types -> it will take the min number, as below min(3,2)=2
different_lengths = [*zip(names[:3], primary_types[:2])]
# print(*different_lengths, sep='\n')

from collections import Counter

# Collect the count of primary types
type_count = Counter(primary_types)
# print(type_count, '\n')

# Collect the count of secondary_types
gen_count = Counter(secondary_types)
# print(gen_count, '\n')

# Use list comprehension to get each name starting letter
starting_letters = [name[0] for name in names]
# print(starting_letters)

starting_letters_count = Counter(starting_letters)
# print(starting_letters_count)

################# USE COMBINATION ############
# Import combination from itertools
from itertools import combinations

pokemon = [1, 2, 3, 4, 5]

# Create a combination object with pairs of pokemon
combos_obj = combinations(pokemon, 2)
# print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
# print(combos_2)

###################### USE SET ###############
ash_pokedex = [1, 2, 3, 4, 5]
misty_pokedex = [1, 7, 2, 10, 3]
# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokemon that exist in the both sets
both = ash_set.intersection(misty_set)
# print(both)

# FInd Pokemon that Ash has and Misty does not
ash_only = ash_set.difference(misty_set)
# print(ash_only)

# Find Pokemon that Ash does not have but Misty has
misty_only = misty_set.difference(ash_set)
# print(misty_only)

# Find the Pokemon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
# print(unique_to_set)

########## SEARCHING FOR POKEMON ############
brock_pokedex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Convert list to a set
brock_pokedex_set = set(brock_pokedex)
# print(brock_pokedex_set)

# Check if 1 is in Ash's list and Brock's set --> True or False
# print(1 in ash_pokedex)
# print(1 in brock_pokedex_set)

# Check if 7 in Ash's list and Brock's set
# print(7 in ash_pokedex)
# print(7 in brock_pokedex_set)

### ---->>>>>> Note: searching in a set is faster than searching in a list

#############################################
def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques


# Use this function to collect unique Pokemon names
names = [1, 1, 3, 4, 5, 5, 6, 6, 7]
uniq_names_func = find_unique_items(names)
# print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokemon names
uniq_names_set = set(names)
# print(len(uniq_names_set))

# Check that both unique collection are equivalent
# print(sorted(uniq_names_func) == sorted(uniq_names_set))

# ---->>>>>> efficient way to gather unique times is to use set

##########################
poke_names = ["adfd", "bdfdf", "csssss", "dsdfdsdf"]
poke_gens = [1, 1, 2, 3]
# Collect Pokemon that belong to generation 1 or generation 2 using list comprehension
gen1_gen2_pokemon = [name for name, gen in zip(poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list use unpack syntax(* - star)
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

# print(gen1_gen2_name_lengths)

###### Now try using for loop to have the same result, but using above method will be faster
gen1_gen2_name_lengths_loop = []

for name, gen in zip(poke_names, poke_gens):
    if gen < 3:
        name_length = len(name)
        poke_tuple = (name, name_length)
        gen1_gen2_name_lengths_loop.append(poke_tuple)

# print(gen1_gen2_name_lengths_loop)
# print(gen1_gen2_name_lengths_loop[:2]) # Print 2 first items of the list

##### POKEMON TOTALS AND AVERAGES WITHOUT A LOOP
# Create a 2-D numpy array
import numpy as np

names = ["adfd", "bdfdf", "csssss"]
stats = np.array([[30, 20, 100], [10, 10, 50], [5, 100, 1000]])
# print(type(stats))

# Create a total stats array (sum of each row by using axis=1; sum of each column by using axis=0)
total_stats_np = np.sum(stats, axis=1)
# print(total_stats_np)

# Create an average stats array
avg_stats_np = np.mean(stats, axis=1)
# print(avg_stats_np)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]


# print(*poke_list_np[:2], sep='\n') # Print 2 first pokemon
### Try using for loop and compare result with above method
poke_list = []

for pokemon, row in zip(names, stats):
    total_stats = np.sum(row)
    avg_stats = np.mean(row)
    poke_list.append((pokemon, total_stats, avg_stats))

# print(poke_list_np == poke_list,'\n') # return true or false

# print(*poke_list_np, sep='\n')
# print(*poke_list_np[:2], sep='\n')
# print(*poke_list[:2], sep='\n')
top_2 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[
    :2
]  # sort on 2nd position : total_stats

# print('2 strongest Pokemon:')
# print(*top_2, sep='\n')

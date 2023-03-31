# OPTIMIZE LOOP BY MOVING ONE TIME CALCULATION OUTSIDE THE LOOP
# Import Counter
from collections import Counter

# Collect the count for each generation
generations = [1, 2, 1, 3, 5, 6, 6, 7, 8, 1, 3]
gen_counts = Counter(generations)
# print(gen_counts)

# Improve for loop by moving one time calculation above the loop
total_count = len(generations)
# print(total_count)

for gen, count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    # print('generation {}: count = {:3} percentage = {}'.format(gen, count, gen_percent))


# HOLISTIC CONVERSION LOOP
# Context: Gather all possible pair of Pokemon types and store each of these pairs in a individual list with an enumarated index as the 1st element of each list.
# A list of all possible Pokemon types as below
pokemon_types = [
    [1, "Normal", "Water"],
    [2, "Normal", "Poison"],
    [3, "Poison", "Steel"],
]

# Collect all possible pairs using combination()
from itertools import combinations

possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumarated_tuples
enumerated_tuples = []

# Add a line to append each enumerated_pair_tuple to the empty list above
for i, pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# print(enumerated_tuples)
# Convert all tuples in enumerated_tuples to a list using map with list function
enumerate_pairs = [*map(list, enumerated_tuples)]
print(enumerate_pairs)

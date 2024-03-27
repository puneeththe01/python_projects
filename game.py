from itertools import permutations
import random

# Define the letters
letters = ['a', 'b', 'c', 'd', 'e', 'f']
numbers = []
i = 0
posibilities = []

# Generate all permutations
all_permutations = permutations(letters)

for x in range(720):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    d = random.randint(1, 20)
    e = random.randint(1, 20)
    f = random.randint(1, 20)
    n = [a, b, c, d, e, f]
    numbers.append(n)
    
# Print all permutations
for permutation in all_permutations:
    posibilities.append(permutation)
    
    print(i," ", numbers[i]," ", permutation)
    i += 1



    
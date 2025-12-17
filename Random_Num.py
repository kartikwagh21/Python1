import random

# Random integer
print(random.randint(1, 10))

# Random float (0-1)
print(random.random())

# Random choice from List
items = [10, 20, 30, 40]
print(random.choice(items))

# Shuffle a list
random.shuffle(items)
print(items)

# Random sample (unique values)
print(random.sample(items, 2))
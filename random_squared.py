import random

starting_list = random.sample(range(50), 20)
print(starting_list)

squared_list = []
for num in starting_list:
    squared_list.append(num * num)

print(squared_list)

my_range = range(10)
print(list(my_range))

new_range = range(0,10,2)
print(list(new_range))

# reversed range
rev_range = range(10, 0, -1)
print(list(rev_range))

# !!* add 1 to each element of list

numbers = [9,10,11,12,13]

for i in range(len(numbers)):
    numbers[i] += 1

print(numbers)

# count "o" in string and their indexes

greeting = "Hello, world"

count = 0
indexes = []

for i in range(len(greeting)):
    if greeting[i] == "o":
        count += 1
        indexes.append(i)
print(count, indexes)



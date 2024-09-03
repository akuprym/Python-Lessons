fruits = ["banana", "orange", "apple", "pineapple"]

sorted_fruits = sorted(fruits, key=lambda element: len(element), reverse=True)
print(sorted_fruits)

longest_word = max(fruits, key=lambda element: len(element))
print(longest_word)
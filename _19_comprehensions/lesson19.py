# List of squared nums for range
squares = [x ** 2 for x in range(10)]
print(squares)

# with "if"
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

# with "else"
labelled_numbers = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(labelled_numbers)


# For Dictionaries

square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)

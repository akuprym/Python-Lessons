my_dictionary = {}

my_dictionary["name"] = "Anna"
my_dictionary["age"] = 25
my_dictionary["city"] = "Minsk"

print(my_dictionary)

my_dictionary.get("name", "Emily")
# use func get() if not sure if there's value.
# set default value "Emily" if there's no value. if there's a value -> default value is not used

print(my_dictionary["name"])
print("=======")

# Iteration through dictionary:

for key, value in my_dictionary.items():
    print(key)
    print(value)

print("--------")

for value in my_dictionary.values():
    print(value)

new_dictionary = {
    "country": "Belarus",
    "city": "Uzda"
}

# Merge 2 dictionaries, 1st option:
my_dictionary.update(new_dictionary)

print(my_dictionary)

# Merge 2 dictionaries, 2nd option:
my_dictionary = my_dictionary | new_dictionary

print(my_dictionary)
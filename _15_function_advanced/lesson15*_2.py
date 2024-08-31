# Keyworded arguments

def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key)
        print(value)

person = {
        "name": "Anna",
        "age": 25
}

# introduce(name="Anna", age=25)

introduce(**person)  # add dict to func arguments

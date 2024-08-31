# Func that returns multiple values

def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified

person = {
        "name": "Anna",
        "age": 25
}

person1, was_modified1 = modify_dict(old_dict=person, name="Anna")

print(person1)
print(was_modified1)
print(type(person1))

person2, was_modified2 = modify_dict(old_dict=person, city="Minsk")

print(person2)
print(was_modified2)
class Animal:
    a_dict = {
        'key_1': 'Value 1'
    }

    a_list = ['Kane', 'Kalob', 'Gully']

    _private_property = 'This is "private"'


animal = Animal()

print(animal.a_dict)
print(animal.a_list)
print(animal._private_property)

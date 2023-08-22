from typing import List


class Animal:
    some_dict = {
        'key_1': 'Value 1'
    }

    some_list: List[str] = ['Kane', 'Kalob', 'Gully']

    def add_name(self, name: str):
        self.some_list.append(name)
        return self.some_list

    def some_method(self):
        print(self.some_list)

    @property
    def gully(self):
        return self.some_list[2]


animal = Animal()

# print(animal.some_dict)
# animal.some_method()
# gully = animal.gully
# print('The cutest gato of all time is', gully)
animal.add_name('Rhubarb')
print(animal.some_list)

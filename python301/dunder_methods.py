# dunder = Double underscore

class Animal:
    fur_color: str 
    animal_type = 'Unknown'

    def __init__(self, fur_color: str) -> None:
        self.fur_color = fur_color

    def eat(self, food:str|None = None):
        print('I am eating yum yum yum')
        if food:
            print('I am eating', food)

    def speak(self):
        raise NotImplementedError

    def chase(self, animal: str='Gazelle'):
        print('I am chasing a', animal)

    def get_fur_color(self):
        print('Getting fur color', self.fur_color)

class HouseCat(Animal):

    def __init__(self, fur_color: str = 'orange') -> None:
        super().__init__(fur_color)
        print('Fur color was saved to the class Object')
        self.animal_type = 'House cat'
        print(self.animal_type)


    def speak(self):
        print('MEOOOW')

    def eat(self):
        super().eat('salmon')

    def chase(self, animal: str):
        super().chase(animal)
        print(animal, 'was cought')

cat = HouseCat()
cat.get_fur_color()

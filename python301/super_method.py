
class Animal:
    fur_color: str = 'Orange'

    def eat(self, food:str|None = None):
        print('I am eating yum yum yum')
        if food:
            print('I am eating', food)

    def speak(self):
        raise NotImplementedError

    def chase(self, animal: str='Gazelle'):
        print('I am chasing a', animal)

class HouseCat(Animal):
    def speak(self):
        print('MEOOOW')

    def eat(self):
        super().eat('salmon')

    def chase(self, animal: str):
        super().chase(animal)
        print(animal, 'was cought')

cat = HouseCat()
cat.eat()


class Animal:
    fur_color: str = 'Orange'

    def eat(self):
        pass

    def speak(self):
        print('Raawwwrr')

    def chase(self):
        pass


class Tiger(Animal):
    def speak(self):
        print("They're GRRRRRREAT!")

class HouseCat(Animal):
    fur_color = 'Black'
    def speak(self):
        print('Meow')

def getFurColor(animal: Animal):
    print(animal.fur_color)

tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()
getFurColor(cat)

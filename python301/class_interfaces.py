
class Animal:
    fur_color: str = 'Orange'

    def eat(self):
        pass

    def speak(self):
        raise NotImplementedError

    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):
        print('MEOOOW')

cat = HouseCat()
cat.speak()

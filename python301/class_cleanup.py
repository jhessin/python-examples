from typing import List


class Animal:
    fur_color: str = 'Orange'

    def eat(self):
        pass

    def speak(self):
        print('Raawwwrr')

    def chase(self):
        pass


tiger = Animal()

tiger.speak()

def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
        return value
    else:
        value = 3 * number + 1
        print(value)
        return value

def collatzSequence(number):
    while((number) != 1):
        number = collatz(number)

while True:
    try:
        print('Enter a number', end='->')
        collatzSequence(int(input()))
        break;
    except ValueError:
        print('Invalid Input! You must enter a whole number!')

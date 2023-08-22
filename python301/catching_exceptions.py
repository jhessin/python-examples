num = input("Enter a number: ")
num2 = input('Enter a second number: ')
result = None

try:
    num = int(num)
    num2 = int(num2)
    result = num / num2
except ValueError:
    print('One of those numbers was not a valid number')
except ZeroDivisionError:
    print('Numbers could not be divided')
except Exception as e:
    print('Exception was caught')
    print(type(e))

print(result)

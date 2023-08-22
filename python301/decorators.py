def my_decorator(func):
    def wrapper():
        print('Do something here')
        value = func()
        print('Original function is finished')
        return value
    return wrapper

@my_decorator
def myfunc():
    print('My name is Jim')
    return 3.14

print(myfunc())

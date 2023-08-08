def eggs(someParameter: list):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

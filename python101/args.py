def add_numbers(*args: int):
    total = 0
    for num in args:
        total += num
    return total


total = add_numbers(1, 3, 5, 7, 9)
print(total)

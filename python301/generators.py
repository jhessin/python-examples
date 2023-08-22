def my_generator():
    for num in range(50):
        yield num ** num


def all_anomallies():
    for num in range(500):
        if (num ** num) % 100 == 0:
            yield (num, num ** num)


# get the anomallies
# for num, value in all_anomallies():
#     print(num, value)

# all_numbers = list(my_generator())
# print(all_numbers)

# for num in my_generator():
#     print(num)

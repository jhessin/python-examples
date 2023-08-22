# numbers = []
# for num in range(1, 10, 2):
#     numbers.append(num**2)

numbers = [num**2 for num in range(10) if num % 2 == 1]

print(numbers)

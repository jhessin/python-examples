birthdays = {
        'Alice': 'Apr 1',
        'Bob': 'Dec 12',
        'Carol': 'Mar 4',
        }

while True:
	print('Enter a name: (blank to quit)')
	name: str = input()
	if name == '':
		break

	if name in birthdays:
		# print(birthdays[name] + ' is the birthday of ' + name)
		print(f'{birthdays[name]} is the birthday of {name}')
	else:
		# print('I do not have birthday information for ' + name)
		print(f'I do not have birthday information for {name}')
		bday = input('What is their birthday?')
		birthdays[name] = bday
		print('Birthday database updated.')
        

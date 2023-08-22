import requests
# import pprint

i = 1
while True:
    req = requests.get(f'https://swapi.dev/api/people/{i}/')
    i += 1
    if req.status_code != 200:
        break
    person = req.json()

    # pprint.pprint(person)

    print(f'Name: {person["name"]}')
    print(f"Birthyear: {person['birth_year']}")

    print('Films:')
    for film in person['films']:
        req = requests.get(film)
        film = req.json()
        print(f"\t{film['title']}")

# from pprint import pprint
from pokebase import APIResource, cache
import pokebase as pb

cache.API_CACHE


def show_pokemon(pokemon: APIResource):
    # pprint(pokemon.__dict__)
    print('name:')
    print(f"\t{pokemon.name}")
    print('xp:')
    print(f"\t{pokemon.base_experience}")
    print('height:')
    print(f"\t{pokemon.height}")
    print('weight:')
    print(f"\t{pokemon.weight}")
    print('species:')
    print(f"\t{pokemon.species.name}")
    print('abilities:')
    if not len(pokemon.abilities):
        print('\tNone')
    for ability in pokemon.abilities:
        print(f"\t{ability.ability}")
    print("forms:")
    if not len(pokemon.forms):
        print('\tNone')
    for form in pokemon.forms:
        print(f"\t{form.name}")
    print('games:')
    for game in pokemon.game_indices:
        print(f"\t{game.version.name}")


def main():
    while True:
        pokemon_name = input(
            'What pokemon would you like to know about(blank to exit): '
        )
        if not pokemon_name:
            break
        pokemon = pb.pokemon(pokemon_name)
        if not pokemon.id_:
            print(f"{pokemon_name} is not a pokemon - try again!")
            continue
        show_pokemon(pokemon)


if __name__ == '__main__':
    main()

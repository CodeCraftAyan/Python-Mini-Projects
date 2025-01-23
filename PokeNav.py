import requests

base_url = "https://pokeapi.co/api/v2/"

def pokemon_info(name_or_id):
    url = f"{base_url}/pokemon/{name_or_id}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        return pokemon
    else:
        print(f"Something Wrong, Failed to Retrieve Pokemon Data : {response.status_code}")

pokemon_name_or_id = input("Enter Pokemon Name or Pokemon ID =  ").lower()
get_pokemon = pokemon_info(pokemon_name_or_id)

if get_pokemon:
    no_of_move = int(input(f"\nHow many of {get_pokemon["name"].capitalize()}'s moves would you like to see? (Enter 0 to see all)\n>>>  "))
    
    moves = [move['move']['name'] for move in get_pokemon['moves']]
    types = [type_info['type']['name'] for type_info in get_pokemon['types']]
    abilites = [abilities['ability']['name'] for abilities in get_pokemon['abilities']]
    stats = {stat['stat']['name']: stat['base_stat'] for stat in get_pokemon['stats']}
    sprites = get_pokemon['sprites']
    sprites_list = ['front_default', 'back_default', 'front_shiny', 'back_shiny']

    print("\n______________________________")
    print(f"\nName : {get_pokemon["name"].capitalize()}")
    print(f"ID : #{get_pokemon["id"]}")

    print("\n_____ Stats ____\n")
    for stat_name, stat_value in stats.items():
        print(f"{stat_name.capitalize()} : {stat_value}")
    
    print("______________________________")
    print(f"\nSpecies : {get_pokemon["species"]["name"]}")
    print(f"Types : {', '.join(types)}")

    if no_of_move == 0:
        print(f"Moves : {' | '.join(moves)}")
    else:
        print(f"Moves : {' | '.join(moves[:no_of_move])}")

    print(f"Abilities : {' | '.join(abilites)}")
    
    print("\n____ Sprites (Ctrl+click the links to view the images) ____\n")
    for sprite_name in sprites_list:
        if sprite_name in sprites:
            print(f"{sprite_name} : {sprites[sprite_name]}")
        else:
            print(f"{sprite_name} : Not Available")
    
    print("______________________________\n")
else:
    print("Pokemon Not Found!")

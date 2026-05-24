import requests
import json

def build_pokemon_database():
    """
    Build a database mapping each Pokémon to its types.
    Returns a dictionary like {"charizard": ["fire", "flying"], ...}
    """
    pokemon_db = {}

    for type_id in range(1, 20):  # Types 1-19
        url = f"https://pokeapi.co/api/v2/type/{type_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            type_name = data['name']

            # Get all Pokémon for this type
            for pokemon_entry in data['pokemon']:
                pokemon_name = pokemon_entry['pokemon']['name']

                # Add Pokémon to database if not already there
                if pokemon_name not in pokemon_db:
                    pokemon_db[pokemon_name] = []

                # Add this type to the Pokémon's type list
                if type_name not in pokemon_db[pokemon_name]:
                    pokemon_db[pokemon_name].append(type_name)

            print(f"✓ Processed type: {type_name}")
        else:
            print(f"✗ Failed to fetch type {type_id}")

    return pokemon_db


if __name__ == "__main__":
    print("Building Pokémon database...\n")
    pokemon_db = build_pokemon_database()

    print(f"\n✓ Total Pokémon found: {len(pokemon_db)}")

    # Show a few examples
    print("\nExamples:")
    examples = ["charizard", "dragonite", "alakazam", "pikachu", "mewtwo"]
    for pokemon in examples:
        if pokemon in pokemon_db:
            print(f"  {pokemon}: {pokemon_db[pokemon]}")

    # Save to file
    with open('pokemon_database.json', 'w') as f:
        json.dump(pokemon_db, f, indent=2)
    print("\n✓ Pokémon database saved to pokemon_database.json")

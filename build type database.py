import requests
import json

# Fetch type data from PokéAPI for all 19 types
def build_type_database():
    """
    Build a comprehensive type matchup database from PokéAPI.
    Returns a dictionary where each type maps to its damage relationships.
    """
    type_database = {}

    for type_id in range(1, 20):  # Types 1-19
        url = f"https://pokeapi.co/api/v2/type/{type_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            type_name = data['name']

            # Extract all damage relationships
            damage_relations = data['damage_relations']

            type_database[type_name] = {
                'double_damage_from': [t['name'] for t in damage_relations['double_damage_from']],
                'double_damage_to': [t['name'] for t in damage_relations['double_damage_to']],
                'half_damage_from': [t['name'] for t in damage_relations['half_damage_from']],
                'half_damage_to': [t['name'] for t in damage_relations['half_damage_to']],
                'no_damage_from': [t['name'] for t in damage_relations['no_damage_from']],
                'no_damage_to': [t['name'] for t in damage_relations['no_damage_to']],
            }

            print(f"✓ Loaded {type_name}")
        else:
            print(f"✗ Failed to fetch type {type_id}")

    return type_database


if __name__ == "__main__":
    print("Building Pokémon type matchup database...\n")
    type_db = build_type_database()

    print("\n" + "="*50)
    print("Type Database Summary:")
    print("="*50)
    for type_name, relationships in type_db.items():
        print(f"\n{type_name.upper()}:")
        print(f"  - Super-effective against: {relationships['double_damage_to']}")
        print(f"  - Weak to: {relationships['double_damage_from']}")

    # Save to file for later use
    with open('type_database.json', 'w') as f:
        json.dump(type_db, f, indent=2)
    print("\n✓ Type database saved to type_database.json")

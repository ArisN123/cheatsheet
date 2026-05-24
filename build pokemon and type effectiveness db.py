import json

def build_type_effectiveness_database():
    """
    Combine type and Pokémon databases to create final type effectiveness.
    For each Pokémon, calculate damage multipliers from all attacking types.

    For a Pokémon with multiple types:
    - Start all types at x1 multiplier
    - For each defending type the Pokémon has:
      - Apply x2 for types in "double_damage_from"
      - Apply x0.5 for types in "half_damage_from"
      - Apply x0 for types in "no_damage_from"
    - Cross-multiply across all defending types

    Output format organizes by multiplier with all multipliers present (even if empty).
    """

    # Load existing databases
    with open('type_database.json', 'r') as f:
        type_db = json.load(f)

    with open('pokemon_database.json', 'r') as f:
        pokemon_db = json.load(f)

    # Initialize result database
    effectiveness_db = {}

    # For each Pokémon
    for pokemon_name, pokemon_types in pokemon_db.items():
        # Temporary dict to calculate multipliers by attacking type
        damage_multipliers = {}

        # Initialize all types at x1
        for attacking_type in type_db.keys():
            damage_multipliers[attacking_type] = 1.0

        # For each type the Pokémon has, apply defensive modifiers
        for defending_type in pokemon_types:
            type_info = type_db[defending_type]

            # Types that do x2 damage to this defending type
            for attacking_type in type_info['double_damage_from']:
                damage_multipliers[attacking_type] *= 2

            # Types that do x0.5 damage to this defending type
            for attacking_type in type_info['half_damage_from']:
                damage_multipliers[attacking_type] *= 0.5

            # Types that do x0 damage to this defending type
            for attacking_type in type_info['no_damage_from']:
                damage_multipliers[attacking_type] *= 0

        # Reorganize by multiplier (ensure all multipliers present)
        damage_from = {
            'x4.0': [],
            'x2.0': [],
            'x1.0': [],
            'x0.5': [],
            'x0.25': [],
            'x0': []
        }

        for attacking_type, multiplier in damage_multipliers.items():
            # Handle multiplier to key conversion (avoid x0.0 becoming x0.0 instead of x0)
            if multiplier == 0:
                key = 'x0'
            else:
                key = f'x{multiplier}'
            damage_from[key].append(attacking_type)

        effectiveness_db[pokemon_name] = {
            'types': pokemon_types,
            'damage_from': damage_from
        }

    return effectiveness_db


if __name__ == "__main__":
    print("Building type effectiveness database...\n")
    effectiveness_db = build_type_effectiveness_database()

    print(f"✓ Created effectiveness data for {len(effectiveness_db)} Pokémon")

    # Show examples
    examples = ["charizard", "dragonite", "alakazam", "pikachu", "mewtwo"]
    print("\nExamples:")
    for pokemon in examples:
        if pokemon in effectiveness_db:
            print(f"\n{pokemon.upper()} (types: {effectiveness_db[pokemon]['types']}):")
            damage_from = effectiveness_db[pokemon]['damage_from']

            for mult_key in ['x4.0', 'x2.0', 'x1.0', 'x0.5', 'x0.25', 'x0']:
                types_list = damage_from[mult_key]
                if types_list:
                    print(f"  {mult_key}: {types_list}")
                else:
                    print(f"  {mult_key}: []")

    # Save to file
    with open('effectiveness_database.json', 'w') as f:
        json.dump(effectiveness_db, f, indent=2)
    print("\n✓ Effectiveness database saved to effectiveness_database.json")

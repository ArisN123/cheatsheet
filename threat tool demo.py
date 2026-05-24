import json

def check_threat(pokemon1, pokemon2):
    """
    Check if pokemon1 is threatened by pokemon2.
    Threatened means pokemon2 has super-effective moves against pokemon1.
    """

    # Load databases
    with open('effectiveness_database.json', 'r') as f:
        effectiveness_db = json.load(f)

    with open('pokemon_database.json', 'r') as f:
        pokemon_db = json.load(f)

    # Normalize names (lowercase)
    pokemon1 = pokemon1.lower()
    pokemon2 = pokemon2.lower()

    # Check if both Pokemon exist
    if pokemon1 not in effectiveness_db:
        print(f"❌ {pokemon1} not found in database")
        return
    if pokemon2 not in pokemon_db:
        print(f"❌ {pokemon2} not found in database")
        return

    # Get pokemon2's types
    pokemon2_types = pokemon_db[pokemon2]

    # Get pokemon1's damage taken from each type
    pokemon1_weaknesses = effectiveness_db[pokemon1]['damage_from']

    print(f"\n{pokemon1.upper()} vs {pokemon2.upper()}")
    print(f"{pokemon2.upper()} types: {pokemon2_types}")
    print("-" * 50)

    threats = []

    # For each type pokemon2 has, check what damage it does to pokemon1
    for p2_type in pokemon2_types:
        # Find the multiplier for this type against pokemon1
        for multiplier_key, types_list in pokemon1_weaknesses.items():
            if p2_type in types_list:
                # Extract multiplier from key (e.g., 'x2.0' -> 2.0)
                mult_str = multiplier_key[1:]  # Remove 'x'
                if mult_str == '0':
                    multiplier = 0
                else:
                    multiplier = float(mult_str)

                if multiplier > 1:  # Super-effective
                    threats.append((p2_type, multiplier))
                break

    if threats:
        print(f"✓ {pokemon1.upper()} IS THREATENED by {pokemon2.upper()}")
        print("\nThreats:")
        for threat_type, multiplier in threats:
            print(f"  - {threat_type} type moves do x{multiplier} damage")
    else:
        print(f"✗ {pokemon1.upper()} is NOT threatened by {pokemon2.upper()}")

    print()


if __name__ == "__main__":
    pkmn1 = input("Enter first Pokémon: ")
    pkmn2 = input("Enter second Pokémon: ")
    check_threat(pkmn1, pkmn2)
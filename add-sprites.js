const fs = require('fs');
const path = require('path');

const dbPath = path.join(__dirname, 'effectiveness_database.json');
const db = JSON.parse(fs.readFileSync(dbPath, 'utf8'));

const pokemonList = Object.keys(db);
console.log(`Found ${pokemonList.length} Pokémon in database`);
console.log('Fetching sprites from PokeAPI...\n');

let completed = 0;
let failed = 0;

async function fetchAndAddSprites() {
    for (const pokemonName of pokemonList) {
        try {
            // Fetch from PokeAPI
            const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);

            if (!response.ok) {
                console.log(`❌ ${pokemonName} - API returned ${response.status}`);
                failed++;
                continue;
            }

            const data = await response.json();
            const spriteUrl = data.sprites?.other?.['official-artwork']?.front_default;

            if (spriteUrl) {
                db[pokemonName].sprite = spriteUrl;
                completed++;
                if (completed % 10 === 0) {
                    console.log(`✓ ${completed}/${pokemonList.length}`);
                }
            } else {
                console.log(`⚠️  ${pokemonName} - No official artwork sprite found`);
                failed++;
            }

            // Rate limiting - 1 request per 50ms to be safe
            await new Promise(resolve => setTimeout(resolve, 50));
        } catch (error) {
            console.log(`❌ ${pokemonName} - ${error.message}`);
            failed++;
        }
    }

    // Save updated database
    fs.writeFileSync(dbPath, JSON.stringify(db, null, 2));

    console.log(`\n${'='.repeat(60)}`);
    console.log(`✓ Completed: ${completed}`);
    console.log(`❌ Failed: ${failed}`);
    console.log(`Database saved with sprites!`);
    console.log(`${'='.repeat(60)}`);
}

fetchAndAddSprites();

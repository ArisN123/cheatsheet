# VGC Tactical Team Sheet

A professional competitive Pokémon VGC dashboard for analyzing team compositions, type coverage, and battle synergies.

## Features

- **Team Builder**: Construct your 6-Pokémon roster with ability selection
- **Squad Composition Analysis**: View all 15 possible 4-Pokémon combinations ranked by effectiveness
- **Pivot Wheel Synergy**: Analyze defensive switching patterns and offensive coverage between team members
- **Type Coverage Heatmap**: Visual representation of what types your team covers offensively and defensively
- **Enemy Threat Analysis**: Toggle enemy team mode to see how your composition fares against specific threats
- **Individual Member Breakdown**: Deep-dive tactical analysis for each team member with partner recommendations

## Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data**: JSON-based Pokémon effectiveness database
- **Backend**: Node.js (development) / Vercel (production)

## Local Development

```bash
npm start
# Starts server at http://localhost:8000
```

## Deployment

This project is deployed on Vercel. Push to the connected GitHub repository to auto-deploy.

## Data Sources

- Pokémon type effectiveness and stats: Custom database
- Type coverage calculations: Real-time analysis engine
- Ability modifiers: Dynamic damage multiplier system

## Usage

1. **Build Your Team**: Select 6 Pokémon and their abilities in the top section
2. **View Squad Options**: See ranked composition recommendations below
3. **Analyze Synergies**: Check pivot wheels for switching patterns
4. **Optional - Enemy Team**: Toggle to see how your team performs against specific threats
5. **Deep Dive**: Expand individual member breakdowns for detailed analysis

---

Made with 💜 for competitive VGC players

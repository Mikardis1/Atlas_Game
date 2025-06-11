# Atlas Game

**Atlas Game** is a geographic learning game that challenges users to guess the countries of a chosen map (Europe, Asia, USA, South America, or Africa). As users input correct answers, the country names appear on the map. When exiting, a CSV file is generated with the countries that were not guessed, allowing players to review and try again later.

## How It Works

1. Choose a map from the options.
2. Enter the names of countries one by one.
3. Correct answers will appear on the map.
4. If you exit the game, a file named `*_to_learn.csv` will be generated with the countries you missed.

## Folders

- `maps/`: Contains the `.gif` images of the blank maps.
- `files/`: Contains the `.csv` files with coordinates and "to learn" files.

## About the CSV Files

The `.csv` files containing the coordinates for each country were created manually using a custom tool called [Atlas Map Editor](https://github.com/Mikardis1/Atlas-map-editor), developed as a companion project. That editor allowed registering country positions by clicking on blank maps and saving them in structured CSV files, which are now used by this game.

Each file has the structure:



## Installation

Make sure you have Python installed. Then, install the required packages using:

```bash
pip install -r requirements.txt

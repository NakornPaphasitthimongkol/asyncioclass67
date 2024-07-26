import aiofiles
import asyncio
import json
import os

# Define the directories for the JSON input and the moves output
pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    # List of all Pokémon JSON files in the pokemonapi directory
    json_files = [f for f in os.listdir(pokemonapi_directory) if f.endswith('.json')]
    
    for json_file in json_files:
        # Read the contents of the JSON file
        async with aiofiles.open(os.path.join(pokemonapi_directory, json_file), mode='r') as f:
            contents = await f.read()

        # Load it into a dictionary and create a list of moves
        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]

        # Open a new file to write the list of moves into
        async with aiofiles.open(os.path.join(pokemonmove_directory, f'{name}_moves.txt'), mode='w') as f:
            await f.write('\n'.join(moves))

# Run the main function
asyncio.run(main())

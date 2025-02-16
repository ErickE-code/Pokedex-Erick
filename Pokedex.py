

import os
import json
import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "image_url": data["sprites"]["front_default"]
        }
        return pokemon_info
    elif response.status_code == 404:
        print("Error: Pokémon no encontrado.")
        return None
    else:
        print("Error en la solicitud a la API.")
        return None

def save_pokemon_data(pokemon_info):
    pokedex_folder = os.path.expanduser("C:/Users/loren/OneDrive/Documents/UCAMP/Python/pokedex")
    
    if not os.path.exists(pokedex_folder):
        os.makedirs(pokedex_folder)
    
    file_path = os.path.join(pokedex_folder, f"{pokemon_info['name']}.json")
    
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(pokemon_info, file, indent=4)
        print(f"✅ Datos de {pokemon_info['name']} guardados en: {file_path}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

def main():
    pokemon_name = input("Introduce el nombre de un Pokémon: ")
    pokemon_data = get_pokemon_data(pokemon_name)
    
    if pokemon_data:
        print(f"\nInformación de {pokemon_data['name'].capitalize()}:")
        print(f"ID: {pokemon_data['id']}")
        print(f"Altura: {pokemon_data['height']} dm")
        print(f"Peso: {pokemon_data['weight']} hg")
        print(f"Tipos: {', '.join(pokemon_data['types'])}")
        print(f"Habilidades: {', '.join(pokemon_data['abilities'])}")
        print(f"Imagen: {pokemon_data['image_url']}")
        save_pokemon_data(pokemon_data)

if __name__ == "__main__":
    main()


import json
import os
from functions import *

os.system("cls")

pokemons = "pokedex.json"

while True:
    print("Pythondex | Renato Herrera")
    print("-"*50)
    print("1. Buscar pokémon")
    print("2. Salir")
    print("-"*50)
    opc = int(input("Selecciona la opción que deseas: "))

    os.system("cls")
    if opc == 1:
        pokemon = input("Ingresa el pokemon que quieres buscar: ")

        buscar_pokemon(pokemons, pokemon)
    else:
        break
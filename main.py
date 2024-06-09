import os
from functions import *

os.system("cls")

pokemons = "pokedex.json"

while True:
    opc = menu( [1,2] )

    os.system("cls")
    if opc == 1:
        pokemon = input("Ingresa el pokemon que quieres buscar: ")
        buscar_pokemon(pokemons, pokemon)
    else:
        print("Adiós, nos vemos pronto!")
        break

import json
import msvcrt
import os

def error(p_message):
    os.system("cls")
    print(p_message)
    msvcrt.getch()
    os.system("cls")
def pres_tecla(p_message):
    print(p_message)
    msvcrt.getch()
    os.system("cls")

def menu(options):
    while True:
        print("Pythondex | Renato Herrera")
        print("-"*50)
        print("1. Buscar pokémon")
        print("2. Salir")
        print("-"*50)
        try:
            opc = int(input("Selecciona la opción que deseas: "))
            if opc in options:
                break
            else:
                error("ERROR! opción incorrecta!")
        except:
            error("ERROR! debe ser entero!")
    return opc

def buscar_pokemon(p_pokemons, p_pokemon):
    with open(p_pokemons, "r", encoding='utf-8') as archivo:
        lector = json.load(archivo)
        for i in range(len(lector)):
            if p_pokemon.capitalize() == lector[i]["name"]["english"]:
                print("")
                print("Pokemon:")
                print(f"\tID: {lector[i]["id"]}")
                print(f"\tNombre: {lector[i]["name"]["english"]}")
                if len(lector[i]["type"]) == 1:
                    print(f"\tTipo: {lector[i]["type"][0]}")
                else:
                    print(f"\tTipo: {lector[i]["type"][0]}, {lector[i]["type"][1]}")
                print("Base:")
                print(f"\tHP: {lector[i]["base"]["HP"]}")
                print(f"\tAttack: {lector[i]["base"]["Attack"]}")
                print(f"\tDefense: {lector[i]["base"]["Defense"]}")
                print(f"\tSp. Attack: {lector[i]["base"]["Sp. Attack"]}")
                print(f"\tSp. Defense: {lector[i]["base"]["Sp. Defense"]}")
                print(f"\tSpeed: {lector[i]["base"]["Speed"]}")
                print("")
                pres_tecla("Presiona cualquier tecla para continuar...")
                return
        error("ERROR! pokémon no encontrado!")

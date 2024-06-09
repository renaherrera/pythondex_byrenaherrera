import json

def buscar_pokemon(p_pokemons, p_pokemon):
    with open(p_pokemons, "r", encoding='utf-8') as archivo:
        lector = json.load(archivo)
        for i in range(len(lector)):
            if p_pokemon.capitalize() == lector[i]["name"]["english"]:
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
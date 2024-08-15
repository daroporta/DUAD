# 1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.


import json

def open_file(data):
    print(type(data))
    for pokemon in data: #for a pokemon in the variable of python list, access position 0 gets the base key of dic
        print(pokemon)
    return data


def add_new_pokemon(data_1):
    while(True):
        try:
            print("Add the details of your pokemon")
            dict={"name":{"english":str(input("Name: "))},"type":[str(input("Type: "))],
                "base":{"HP":int(input("HP: ")),
                        "Attack":int(input("Attack: ")),
                        "Defense":int(input("Defense: ")),
                        "Sp.Attack":int(input("Sp.Attack: ")),
                        "Sp.Defense":int(input("Sp.Defense: ")),
                        "Speed":int(input("Speed: "))}}

            data_1.append(dict)
            break
        except ValueError as ex:
            print("The value entered is not correct, please try again and type a string for the name and type and an integer for the rest of the data.")
    return data_1


def convert_file(data_2):
    add_json=json.dumps(data_2, indent=2)
    return add_json


def convert_to_json(pokemon):
    with open("pokemon.json", "w") as file:
        file.write(pokemon) #json plus dump means to write the python file into a json. we have to add the name of the data and the name of the file where to write it and indent to read it clearly in the json


with open("pokemon.json") as file: #open the json file as a normal file
        data=json.load(file)#creates a new variable to convert the json file into a python calling json and using load + the file name


open_file(data)
convert_to_json(convert_file(add_new_pokemon(data)))
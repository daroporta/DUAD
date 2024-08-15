# 1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#     1. Debe incluir:
#         1. Nombre
#         2. Género
#         3. Desarrollador
#         4. Clasificación ESRB


import csv  #csv library is imported to use the class csv.DictWriter

def amount_video_games():  #function to know the n amount of games the user wants to add. Returns the amount.
    amount_of_games=int(input("\nPlease indicate the amount of video games you want to add to your CSV file: "))
    return amount_of_games


def add_games_information(): #Function to create a dic. based on the amount entered by user, used for to create the n amount of dic.
    try: #try is for the amount_video_games function that is called, in case the user types a value that is not valid. 
        for times in range(amount_video_games()):
            dictionary={"name":input("Name of the video game: "), "gender":input("Gender: "), 
                        "developer":input("Developer: "), "classification":input("ESRB classification: ") }
            list_of_games.append(dictionary)   #add each dic created to the list. 
        return list_of_games  #returns the list
    except ValueError as ex: #if wrong value is typed for amount of games, user will need to restart the process. 
        print("The value entered is not correct, please try again and type an integer number.")


def add_games_to_csv(path, data, headers):  #adds the information of each dictionary that is inside the list to the cvs file. 
    with open(path, "w", encoding='utf-8') as file: #opens the csv file, path is the file, "w" write mode, opens the file as file (name).
        writer= csv.DictWriter(file, headers) #creates a variable with a class csv.DictWriter (file (csv where info will be written and headers))
        writer.writeheader()#writes the keys to the first row of the csv file 
        writer.writerows(data)#writes the values on the rest of the file from top to bottom. 


def main():
    while(True):#loop to ask the user if they want to continue adding more games. 
        try:  
            add=input("\nDo you want to add games to your csv file (Yes) (No): \n").lower() #will change the str to lower case.
            if add=="yes":
                add_games_information() # call function to add the info of the games. 
                add_games_to_csv("games.csv", list_of_games, list_of_games[0].keys())#adds to the csv, csv created, info from list, user the headers(keys) from the first list. 
            elif add=="no": #if does´nt want to continue adding the program is closed
                print("\nThank you for visiting, bye...")
                break
            else:
                print("\nIncorrect entry, please try again.") # if a different value is enter they need to try
        except Exception as ex:
            print(" ")


list_of_games=[]  #list that will contain the dictionaries with their set keys and entered values. 

main()




#Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

import csv  #csv library is imported to use the class csv.DictWriter

def amount_video_games():  #function to know the n amount of games the user wants to add. Returns the amount.
    amount_of_games=int(input("\nPlease indicate the amount of video games you want to add to your CSV file: "))
    return amount_of_games


def add_games_information(): #Function to create a dic. based on the amount entered by user, used for to create the n amount of dic.
    try: #try is for the amount_video_games function that is called, in case the user types a value that is not valid. 
        for times in range(amount_video_games()):
            dictionary={"name":input("Name of the video game: "), "gender":input("Gender: "), 
                        "developer":input("Developer: "), "classification":input("ESRB classification: ") }
            list_of_games.append(dictionary)   #add each dic created to the list. 
        return list_of_games  #returns the list
    except ValueError as ex: #if wrong value is typed for amount of games, user will need to restart the process. 
        print("The value entered is not correct, please try again and type an integer number.")


def add_games_to_csv(path, data, headers):  #adds the information of each dictionary that is inside the list to the cvs file. 
    with open(path, "w", encoding='utf-8') as file: #opens the csv file, path is the file, "w" write mode, opens the file as file (name).
        writer= csv.DictWriter(file, headers, delimiter="\t") #creates a variable with a class csv.DictWriter (file (csv where info will be written and headers))  added delimited \t to separate with tabs instead of commas
        writer.writeheader()#writes the keys to the first row of the csv file 
        writer.writerows(data)#writes the values on the rest of the file from top to bottom. 


def main():
    while(True):#loop to ask the user if they want to continue adding more games. 
        try:  
            add=input("\nDo you want to add games to your csv file (Yes) (No): \n").lower() #will change the str to lower case.
            if add=="yes":
                add_games_information() # call function to add the info of the games. 
                add_games_to_csv("games.csv", list_of_games, list_of_games[0].keys())#adds to the csv, csv created, info from list, user the headers(keys) from the first list. 
            elif add=="no": #if does´nt want to continue adding the program is closed
                print("\nThank you for visiting, bye...")
                break
            else:
                print("\nIncorrect entry, please try again.") # if a different value is enter they need to try
        except Exception as ex:
            print(" ")


list_of_games=[]  #list that will contain the dictionaries with their set keys and entered values. 

main()
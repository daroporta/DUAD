#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
def open_file(path):
    with open(path) as file: #opens file in read mode by default
        for line in file.readlines(): #using readlines, gives me a list. For, prints each line. 
            print(line.replace("\n", ""))# replace the newline with a space


def create_file(path):  #parameter, will get the original list
    with open(path) as file: # opens the original lists
        with open("new_file.txt", "w") as data: #by default when w is used, if no file exists the system will create it.
            for line in file: #for each line in the original file
                data.write(line)#write the line in the new file. 


def order_alphabetically():
    with open("new_file.txt", "r") as data:#opens the new file and reads its information
        names=data.readlines()#creates a variable which will read each line of the new file in a list format. 
    names.sort()#file closed, now the variable which contains the list sorts the data alphabetically
    with open("new_file.txt", "w") as data:#opens again the file in write mode
        for line in names:#for each line in the variable names(list)
            data.write(line)#write the line in the data file(same new file)


open_file('List_of_songs.txt')

create_file('List_of_songs.txt')

order_alphabetically()
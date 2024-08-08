#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.


def print_one():
    name=input("Please enter your first name: ")
    print(f"Hello {name}")


def print_two():
    print_one()  #second function calls the first one
    age=int(input("Please enter your age: "))
    print(f"Your age is: {age}")

print_two() #second function is called. 

#--------------------------------------------------------------------------------------------
#Experimente con el concepto de scope:

#a)Intente acceder a una variable definida dentro de una función desde afuera.

def define_variable():
    variable= 900*900 #Variable definida dentro de la función defined_variable
    print(variable) #Intento de acceder a la variable desde afuera. 

#NameError: name 'variable' is not defined. Did you mean: 'callable'? #Da un error al ser una variable local, solo se puede acceder al llamar la función

#b) Intente acceder a una variable global desde una función y cambiar su valor.

def update_location():
    location=input("Please enter your new location: ")  #Variable global con nuevo valor. 
    print(f"Your new address is: {location}")

location="Your current location is: Costa Rica, Limón, Pococí"  #Variable global

update_location() #Se llama a la función con el nuevo valor de la variable global. 

#--------------------------------------------------------------------------------------------

# #1. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41

def sum_of_list(list_of_numbers):
    sum_of_numbers=0
    for num in list_of_numbers:
        sum_of_numbers= sum_of_numbers + num
    print(f"The sum of all the numbers is: {sum_of_numbers}")

sum_of_list([1,2,3,4])

#--------------------------------------------------------------------------------------------

#Cree una función que le de la vuelta a un string y lo retorne.

def return_string(word):
    space= " "
    for letter in range(-1, -len(word) -1, -1):
        space=space+word[letter]+" "
    print(space)

return_string(input("Please type your string: "))

#--------------------------------------------------------------------------------------------
#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def upper_and_lower(your_string):
    upper_letter= 0
    lower_letter=0
    space=0
    for letter in your_string:
        if letter.isupper():
            upper_letter += 1
        elif letter.islower():
            lower_letter += 1
        else:
            space +=1
    print(f"Your string has {upper_letter} upper letter(s)")
    print(f"Your string has {lower_letter} lower letter(s)")


upper_and_lower(input("Please type your string: "))

#--------------------------------------------------------------------------------------------
#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def order_words(list_of_words):
    words_split=list_of_words.split("-")
    words_split.sort()
    words_with_dash= "-".join(words_split)
    return words_with_dash


list_of_words=input("Please enter the amount of words for your list separated by dash: ")

print(order_words(list_of_words))

#--------------------------------------------------------------------------------------------
#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def add_numbers():
    amount_of_numbers=int(input("How many numbers would you like to add to the list?: "))
    amount_number=1 #should add at least 1 number

    while amount_number <= amount_of_numbers: #from 1 to the amount the user added. 
        numbers=int(input("Please type an integer number: "))
        list_of_numbers.append(numbers)# add each number to the list of numbers
        amount_number += 1 #add one to each loop until it reaches the amount the user added. 

    return list_of_numbers #returns the list with the numbers the user added. 


def get_prime():
    for number in list_of_numbers:  #for each number in list
        cont= 0  # add the amount of numbers that are divided and the result is 0
        for each_number in range (1, number + 1): # from 1 to the number (+1 to add the number that is being tested)
            if number % each_number==0: # if the number divided by all the numbers lesser than the number that is being tested is equal to 0
                cont+=1  # add 1 to the counter

        if cont==2: # if the number only has two results of 0 when divided by  it is prime
            prime_numbers.append(number)# add the number to the list of prime
        
    return prime_numbers #return the list with the numbers that are prime


list_of_numbers = []
prime_numbers = []

add_numbers() #call first fuction to add the numbers to the list
print(get_prime())# second function to loop the list and determine prime numbers and add them to a new list
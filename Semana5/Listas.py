#1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.


first_list = ["Hay", "en", "que", "iteración", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for index in range(1):
    for index in range(0, len(second_list)):
        print(first_list[index], second_list[index])


#-----------------------------------------------------------------------------------------------
#1. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.


my_string= "Pizza con Piña"    #https://datagy.io/python-range/
for index in range(-1, -len(my_string)-1, -1):
    print(my_string[index])

#-----------------------------------------------------------------------------------------------
#1. Cree un programa que intercambie el primer y último elemento de una lista. Debe funcionar con listas de cualquier tamaño.


my_list = [4, 3, 6, 1, 7]

index=-1
index_1=0

print(my_list[index], my_list[index_1])

#-----------------------------------------------------------------------------------------------
#1. Cree un programa que elimine todos los números impares de una lista.


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index, number in enumerate(my_list):
    even= number % 2
    if even == 0:
        print(number)

#-----------------------------------------------------------------------------------------------
#1. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del número ingresado más alto.


print("\nPlease enter 10 numbers\n")

list_of_number=[]

for number in range(10):
    user_number= float(input("Type a number: "))
    list_of_number.append(user_number)

largest_number=list_of_number[0]

for number in list_of_number:
    if number > largest_number:
        largest_number=number

print(f"The list is {list_of_number} and the largest number is: {largest_number}")


# Cree una calculadora por línea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo número actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción inválida, o si ingresa un número inválido a la hora de hacer la operación.


def delete_result():
    number[0]=0
    print("\nValue deleted.")


def division_of_number():
    try:
        divided_number=number[0]  / new_number()
        number[0] = divided_number
        print(f"Result of division: {divided_number}")
        return divided_number
    except ZeroDivisionError as ex:
        print(f"\nThere was an error in your mathematical operation: {ex}")    #in case user divides by 0


def multiplication_of_number():
    number_multiplied=number[0]  * new_number()
    number[0] = number_multiplied
    print(f"Result of multiplication: {number_multiplied}")
    return number_multiplied


def subtract_number():
    number_subtracted=number[0] - new_number()
    number[0]=number_subtracted
    print(f"Result of subtraction: {number_subtracted}")
    return number_subtracted


def sum_number():
    number_with_sum=number[0]+ new_number()
    number[0]=number_with_sum
    print(f"Result of sum: {number_with_sum}")
    return number_with_sum


def new_number():
    while True:
        try:
            new_digit=float(input("\nPlease enter the new number: ")) #give the option to enter float numbers
            return new_digit
        except ValueError as ex:
            print(f"\nIncorrect value: {ex}, try again")  #in case the user enters a value other than a number, allows integer


def menu():
    while (True):
        try:
            print(f"\nCalculator\n\n1.Sum\n2.Subtraction\n3.Multiplication\n4.Division\n5.Delete Result\n6.Exit\n\nCurrent number:{number}\n")
            option=int(input("Please select the type of operation you want to execute: "))
            if option == 1:
                sum_number()
            elif option == 2:
                subtract_number()
            elif option == 3:
                multiplication_of_number()
            elif option == 4:
                division_of_number()
            elif option == 5:
                delete_result()
            elif option == 6:
                break
            else:
                print("Incorrect option, try again")
        except Exception as ex:
            print(f"\nThere was an error: {ex}, please try again") #in case the input is not a number. 


number=[0] #list to add, update and remove the current_value
menu()
age=int((input("Ingrese el nÃºmero de su edad en aÃ±os: ")))
name=input("Ingrese su primer nombre: ")
last_name=input("Ingrese su apellido: ")

if age < 0:
    print("Valor incorrecto, usted no puede tener menos de 0 aÃ±os.")
elif age < 6:
    print(f"{name} {last_name} usted es un bebÃ©.")
elif age < 12:
    print(f"{name} {last_name} usted  es un niÃ±o.")
elif age < 16:
    print(f"{name} {last_name} usted  es un preadolescente.")
elif age < 20:
    print(f"{name} {last_name} usted  es un adolescente.")
elif age < 30:
    print(f"{name} {last_name} usted  es un joven.")
elif age < 60:
    print(f"{name} {last_name} usted  es un adulto.")
else:
    print(f"{name} {last_name} usted  es un adulto mayor.")

#---------------------------------------------------------------------

secret_number= 7
user_number= int(input("Type a number from 1 to 10: "))

while secret_number != user_number:
    print("Unfortunately, that is not the right number, please try again.")
    user_number= int(input("Type a number from 1 to 10: "))

print("You have guessed the right number, congratulations")

#--------------------------------------------------------------------------

number_1=float(input("Type your first number: "))
number_2=float(input("Type your second number: "))
number_3=float(input("Type your third number: "))

                                    # if number_1 > number_2 and number_1 > number_3:
                                    #     print(f"The greatest number is {number_1}")
                                    # elif number_2 > number_1 and number_2 > number_3:
                                    #     print(f"The greatest number is {number_2}")
                                    # else:
                                    #     print(f"The greatest number is {number_3}")

if number_1 > number_2:
    if number_1 > number_3:
        print("Number one is the greatest")
    else:
        print("Number three is the greatest")
elif number_2 > number_1:
    if number_2 > number_3:
        print("Number two is the greatest")
    else:
        print("Number three is the greatest")
else:
    print("Please enter numeric values, try again")

#-------------------------------------------------------

contador=1
notas_aprobadas=0
notas_desaprobadas=0
promedio_aprobadas=0
promedio_desaprobadas=0
promedio_notas_total=0

total_de_notas=int(input("Ingrese el total de notas: "))

while contador <= total_de_notas:
    nota=float(input("Ingrese la nota:"))
    if nota >= 70:
        notas_aprobadas = notas_aprobadas + 1
        promedio_aprobadas = promedio_aprobadas + nota
    else:
        notas_desaprobadas = notas_desaprobadas + 1
        promedio_desaprobadas = promedio_desaprobadas + nota
    promedio_notas_total = promedio_notas_total + nota
    contador= contador + 1
promedio_notas_total = promedio_notas_total / nota
promedio_aprobadas = promedio_notas_total / notas_aprobadas
promedio_desaprobadas=promedio_desaprobadas / notas_desaprobadas

print(f"Cantidad de notas aprobadas: {notas_aprobadas}")
print(f"Cantidad de notas desaprobadas: {notas_desaprobadas}")

print(f"Promedio de notas aprobadas: {promedio_aprobadas}")
print(f"Promedio de notas desaprobadas: {promedio_desaprobadas}")
print(f"Promedio de notas totales: {promedio_notas_total}")
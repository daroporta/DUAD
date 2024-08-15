# Cree un diccionario que guarde la siguiente información sobre un hotel:
# nombre
# numero_de_estrellas
# habitaciones
# El key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
# numero
# piso
# precio_por_noche

diccionario_de_hotel= {
    "nombre":"N/A",
    "numero_de_estrellas":0,
    "habitaciones":[],
}

solicita la información que se agregara al primer diccionario
diccionario_de_hotel["nombre"]= input("Escriba el nombre del hotel: ")
diccionario_de_hotel["numero_de_estrellas"]=int(input("Escriba el número de estrellas del hotel: "))
cantidad_de_habitaciones=int(input("Ingrese la cantidad de habitaciones: ")) #cantidad de habitaciones que se agregaran en la lista


#ciclo for para agregar la informacion de cada habitación
for habitacion in range(cantidad_de_habitaciones):
    habitaciones = {"numero_de_habitacion": 0,   #creacion de nuevo dic. que se agrega a la lista. 
        "numero_de_piso":0,
        "precio_por_noche":0.0}
    
    print("\nDatos de la habición", habitacion+1)

    numero_de_habitacion=int(input("\nEscriba el número de la habitación: "))
    habitaciones["numero_de_habitacion"]=numero_de_habitacion

    piso_de_habitacion=int(input("Escriba el número del piso: "))
    habitaciones["numero_de_piso"]=piso_de_habitacion

    precio_por_noche=float(input("Escriba el precio por noche: "))
    habitaciones["precio_por_noche"]=precio_por_noche

    diccionario_de_hotel["habitaciones"].append(habitaciones)


print(diccionario_de_hotel.items())


#------------------------------------------------------------------------------

#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_one=["first_name", "last_name","age","job"]
list_two=[]

name=input("Please enter your first name: ")
last_name=input("Please enter your last name: ")
age=int(input("Please enter your age: "))
job=input("Please enter your job: ")

list_two.append(name)
list_two.append(last_name)
list_two.append(age)
list_two.append(job)

dictionary={list_one[0]:list_two[0], list_one[1]:list_two[1], list_one[2]:list_two[2], list_one[3]:list_two[3]} #first option

print(dictionary)

#------------------------------------------------------------------------------

#Cree un programa que use una lista para eliminar keys de un diccionario.

list_of_keys=["age", "access_level"]
employee={"name":"John", "email":"john@corp.com", "age":"30","access_level":"5"}

employee.pop(list_of_keys[0])
employee.pop(list_of_keys[1])

print(employee)


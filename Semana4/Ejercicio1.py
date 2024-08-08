#1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
    #1. Por ejemplo:

        #1. string + string → Sí, se pueden sumar, ya que funciona como una concatenación. 
        
string_string= "hello" + "world"
print(string_string)

#helloworld

#------------------------------------------------------------------------------       
#1. string + int → No se puede sumar un string con un número entero (interger).
        

string_interger= "hola" + 5
print(string_interger)
        
        #TypeError: can only concatenate str (not "int") to str


#------------------------------------------------------------------------------  
#1. int + string → Al igual que el anterior, el operador no funciona al sumar int + str. 
        

interger_string= 45 + "Sumado"
print(interger_string)
        
        #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#------------------------------------------------------------------------------  
        
#1. list + list → La suma de dos listas sí funciona sin importar los tipos de datos que estén dentro. 
        
lista_lista= ["manzanas", "papas", "zanahorias", + 5 + 2.1] + [False, "cebolla", "tomate", 8, 10.50]
print(lista_lista)
        
['manzanas', 'papas', 'zanahorias', 7.1, False, 'cebolla', 'tomate', 8, 10.5]

#------------------------------------------------------------------------------        
#1. string + list → No se puede sumar un string a una lista. 
        
string_lista= "casa" + ["cuarto", "baño", "cocina", 2.50]
print(string_lista)
        
        #TypeError: can only concatenate str (not "list") to str
 
#------------------------------------------------------------------------------        
#1. float + int → Sí se pueden sumar dos números, sin importar si tienen decimales o son enteros. 
        
decimales_enteros= 45.780 + 5
print(decimales_enteros)
        
50.78

#------------------------------------------------------------------------------ 
#1. bool + bool → Sí se pueden sumar booleanos, sin embargo, la suma de un verdadero con un falso, o un falso con un verdadero se tomará como un valor binario. Por lo contrario, un verdadero más verdadero suma 2, ya que sería el valor de 1 más 1. 
        
boolean_boolean= False+False
boolean_boolean2=False+True
boolean_boolean3=True+True
boolean_boolean4=True + False
        
print(boolean_boolean)
print(boolean_boolean2)
print(boolean_boolean3)
print(boolean_boolean4)
        
0
1
2
1


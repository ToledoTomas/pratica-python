#COMENTARIOS
# print("Hello world!")

#VARIABLES
# x = 5
# y = "John"
# print(x)
# print(y)

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# VALORES MULTIPLES
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# fruits = ["Orange", "Banana", "Cherry"]
# x,y,z = fruits
# print(x)
# print(y)
# print(z)

# VARIABLE GLOBAL
# x = "Awesome"

# def myFunc():
#     global x
#     x = "Fantastic"

# myFunc()

# print("Python is", x)

#NUMBERS
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# import random

# print(random.randrange(1, 100))

# STRINGS
# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#     print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# b = "Hello, World!"
# print(b[2:5])

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.lower())

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

#  CALCULADORA
# n1 = input("Ingresa el primer numero: ")
# n2 = input("Ingresa el segundo numero: ")

# n1 = int(n1)
# n2 = int(n2)

# suma = n1 + n2
# resta = n1 - n2
# multi = n1 * n2
# divi = n1 / n2

# print(f"""
# El resultado de la suma es {suma}
# El resultado de la resta es {resta}
# El resultado de la multiplicacion es {multi}
# El resultado de la division es {divi}
# """)


# print("Bienvenido a la calculadora")
# num1 = input("Ingresa el primer numero: ")

# num1 = int(num1)

# while num1:
#     operacion = input("Ingresa una operacion (suma, resta, multiplicacion o division) o ingresa exit para salir: ")


#     if operacion.lower().strip() == "suma":
#         num2 = input("Ingresa el segundo numero: ")

#         num2 = int(num2)

#         total = num1 + num2

#         print(f"El resultado de la suma es {total}")
    
#         num1 = total

#     if operacion.lower().strip() == "resta":
#         num2 = input("Ingresa el segundo numero: ")

#         num2 = int(num2)

#         total = num1 - num2

#         print(f"El resultado de la resta es {total}")
    
#         num1 = total

#     if operacion.lower().strip() == "division":
#         num2 = input("Ingresa el segundo numero: ")

#         num2 = int(num2)

#         total = num1 / num2

#         print(f"El resultado de la division es {total}")
    
#         num1 = total

#     if operacion.lower().strip() == "multiplicacion":
#         num2 = input("Ingresa el segundo numero: ")

#         num2 = int(num2)

#         total = num1 * num2

#         print(f"El resultado de la multiplicacion es {total}")
    
#         num1 = total
    
#     if operacion.lower().strip() == "exit":
#         break


# OPERADORES LOGICOS
# gas = False
# encendido = False
# precio = 8

# if gas or encendido or precio > 8:
#     print("Puedes avanzar")

# FOR
# buscar = 11
# for numero in range(6):
#     print(numero)
#     if numero == buscar:
#         print("Numero encontrado: ", numero)
#         break
# else: print("No se encontro el numero")

# for char in "Esto es un string":
#     print(char)

# LISTAS
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# print(type(list1))

# COLECCIONES
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


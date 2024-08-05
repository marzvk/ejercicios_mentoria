# # # VARIABLES , operadores , expresiones , condicionales y bucles  # # # #

# 1) Hacer un programa donde se pida un nombre por teclado y se imprima “Hola
# ..el_nombre_ingresado”

# nombre = input('ingrese su nombre: ')
# print("hola",nombre)

# 2) Hacer un programa que solicite por teclado dos número y muestre la suma , la resta ,la
# multiplicación y la división de esos números

# num_1 = int(input('ingrese primer numero: '))
# num_2 = int(input('ingrese segundo numero: '))
# print('la suma de los numeros es: ',num_1 + num_2)
# print('la resta de los numeros es: ',num_1 - num_2)
# print('la multiplicacion de los numeros es: ',num_1 * num_2)
# print('la division de los numeros es: ',num_1 / num_2)

# 3) Hacer un programa que solicite una edad y determine si es mayor de edad.

# edad = int(input('ingrese su edad: '))
# if edad >= 18:
#     print('usted es mayor de edad')
# else:
#     print('usted es menor de edad: ')

# 4) Hacer un programa que solicite una edad e imprima “Es mayor” si es mayor de edad ,
# sino que imprima “Es menor”.

# 5) Hacer un programa que solicite un color por teclado e imprima “Puede pasar “ si el
# color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ si es rojo o “Color
# inválido” si es cualquier otro.

# color = input("Ingresar un color: ")

# if color == "verde":
#     print("Puede pasar")
# elif color == "amarillo":
#     print("Precaución")
# elif color == "rojo":
#     print("No pasar")
# else:
#     print("Color inválido")

# 6) Hacer un programa que cuente desde el 1 al 100 y los imprima uno a uno.

# for num in range(101):
#     print(num)

# 7) Hacer un programa que cuente del 1 al 100 inclusive e imprima sólo los números pares

# for num in range(1,101):
#     if num % 2 == 0:
#         print(num)

# 8) Hacer un programa que cuente del 1 al 100 inclusive e imprima los números que son
# divisibles por 2 y por 5.

# for num in range(1,101):
#     if num % 2 == 0 and num % 5 == 0:
#         print(num)

# 9) Hacer un programa que imprima una tabla de multiplicar del 2 al 9 . Cada uno debe
# mostrar sus valores multiplicados del 1 al 9 inclusive

# for num in range(2,10):
#     for i in range(1,10):
#         print(i * num,end=' ')
#     print('\n')

# 10) Hacer un programa que muestre el siguiente dibujo.
#  * * * * * * * * * *
#  * * * * * * * * * *
#  * * * * * * * * * *
#  * * * * * * * * * *
#  * * * * * * * * * *

# for i in range(1,6):
#     for j in range(1,11):
#     #    print('*',end=' ')
#     print()

# 11) Hacer un programa donde se muestre el siguiente dibujo

#  * * * * * * * * * *
#  * *
#  * *
#  * *
#  * * * * * * * * * *

# tete = [10,2,2,2,10]
# for num in tete:
#     print('* ' * num)

# 12)Hacer un programa que muestre el siguiente dibujo
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *

# for i in range(6):
#     print(i * '* ',end='\n')

# 13) Idem anterior con este dibujo
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

# for i in range(5,0,-1):
#     print(i*'* ',end='\n') # espacio despues del string asterisco para separar




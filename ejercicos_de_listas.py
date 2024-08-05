# # # '''Ejercicios de listas (Utilizar todo lo aprendido hasta la ultima clase)

# Ejer junto con su cuadrado y su cubo.

# lista_10 = [1,cicio 1
# Realizar un programa que inicialice una lista con 10 valores
# aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento
# de la lista2,3,4,5,6,7,8,9,10]
# for i in lista_10:
#     print('el elemento es: ',i,'\n','su cuadradado es:',i**2,'\n','su cubo es:',i**3,'\n')

# Ejercicio 2
# Crea una lista e inicializala con 5 cadenas de caracteres ingresadas
# por teclado. Copia los elementos de la lista en otra lista pero en orden inverso,
# y muestra sus elementos por la pantalla.

# lista = []
# for i in range(5):
#     lista.append(input('ingrese cadena: '))
# print(lista)
# nueva_lista = lista.copy()
# print(nueva_lista)
# nueva_lista.reverse()
# print(nueva_lista)

# Ejercicio 3
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas
# por un alumno (comprendidas entre 0 y 10).
# A continuación debe mostrar todas las notas, la nota media,
# la nota más alta que ha sacado y la menor.

# notas = []
# for nota in range(5):
#     notas.append(int(input('ingrese una nota: ')))
# notas_medias = sum(notas)/len(notas)
# print(notas)
# print(notas_medias)
# print('el minimo es: ',min(notas),', y el maximo es: ', max(notas))

# Ejercicio 4
# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos
# un número negativo.
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

# lista_num = []

# while True:
#     numero = int(input('ingrese algun numero: '))
#     if numero >= 0:
#         lista_num.append(numero)
#     else:
#         break
# print(lista_num)
# # # # # #   Ejercicios de Diccionarios # # # # # ## #  #

# # Ejercicio 1
# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

num = int(input('ingrese un numero: '))
dic = {}
for i in range(1,num+1):
    dic[i] = i**2
# print(dic)

# # Ejercicio 2
# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

dic = {}
texto = (input('ingrese texto: ')).lower()
for i in texto:
    if i != ' ':
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
# print(dic)

# # Ejercicio 3
# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
# Extra crear una lista con el total de la compras.

dic = {
    'manzana': 5000,
    'banana': 2500,
    'pera': 8000,
    'uva': 5000,
    'mandarina': 2500,
    'naranja': 3000
}
lista_de_compras = {}
while True:

    print()
    print('Bienvenido a su Verduleria')
    print('Que desea hacer ?')
    print('>>> MENU <<<')
    print('>>> 1. Compras')
    print('>>> 2. Agregar fruta')
    print('>>> 3. Eliminar fruta')
    print('>>> 4. Modificar precio')
    print('>>> 5. Mostrar precio por kg')
    print('>>> 6. Mostrar total de la compra')
    print('>>> 7. Salir')
    print()
    opcion = input('Ingrese una opcion: ')

    if opcion == "1":
        print('Eligio COMPRAS')
        nombre_fruta = (
            input('ingrese nombre de fruta que quiere comprar: ')).lower()
        if nombre_fruta in dic:
            cantidad = float(input('Ingrese cantidad de kg que desea: '))
            total = dic[nombre_fruta] * cantidad
            print(
                f'Fruta: {nombre_fruta}\tCantidad en kg: {cantidad}\nEl total a pagar es: ${total}'
            )
            if nombre_fruta in lista_de_compras:
                lista_de_compras[nombre_fruta] += total
            else:
                lista_de_compras[nombre_fruta] = total
        else:
            print('error: la fruta no existe')
    elif opcion == "2":
        print('Elegiste AGREGAR FRUTA')
        nombre_fruta = (input('ingrese nombre de la fruta nueva: ')).lower()
        if nombre_fruta in dic:
            print('La fruta ya existe, pruebe opcion modificar precio: ')
        else:
            precio_fruta = int(input('Ingrese precio: '))
            dic.update({nombre_fruta: precio_fruta})
    elif opcion == "3":
        print('Elegiste ELIMINAR FRUTA')
        sacar = (input('ingrese nombre de fruta a eliminar: ')).lower()
        if sacar in dic:
            dic.pop(sacar)
            print(dic)
        else:
            print('La fruta no existe, eliga otra: ')
    elif opcion == "4":
        print('Elegiste MODIFICAR PRECIO')
        nombre_fruta = (input('ingrese nombre de fruta: ')).lower()
        if nombre_fruta in dic:
            precio_fruta = int(input("ingrese precio de la fruta: "))
            dic[nombre_fruta] = precio_fruta
            print(dic)
        else:
            print('La fruta no existe')
    elif opcion == "5":
        print('Elegiste MOSTRAR PRECIO POR KG')
        print(dic)
    elif opcion == '6':
        print('Eligio TOTAL DE SU COMPRA ACTUAL')
        print()
        pago = []
        for clave , valor in lista_de_compras.items():
            print(f'{clave} : $ {valor}')
            pago.append(valor)
        print('---------------------')
        print(f'El total a pagar es: {sum(pago)}')
    elif opcion == "7":
        break

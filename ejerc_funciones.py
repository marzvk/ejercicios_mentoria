# # # # # FUNCIONES Y MODULO


# 3-Crea una función llamada invertir_cadena que tome una cadena de texto como parámetro
# y devuelva la cadena invertida.

def invertir_cadena(cadena):
    return cadena[::-1]

# print(invertir_cadena('mario'))

#----------------------------------------------------

# Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba
# centrado en pantalla (suponiendo una anchura de 80 columnas;
# pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje
# utilizando el carácter =.

def escribir_centrado(texto):
    longitud = len(texto)
    espacios = 40 - longitud // 2
    print(" " * espacios,texto)
    print(" " * espacios,"=" * longitud)

# escribir_centrado('super mario bros')

#--------------------------------------------------------

# Crea una función llamada promedio que tome una lista de números como parámetro y
# devuelva el promedio de esos números.

numeros = [2,5,7,89,6,4,5]
def promedio(lista_numeros):
    return sum(lista_numeros)/len(lista_numeros)

# print(promedio(numeros))
#------------------------------------------
def es_palindromo(texto):
    if texto == texto[::-1]:
        salida = True
    else:
        salida = False
    return salida
# print(es_palindromo('orol'))

#----------------------------------------
def encontrar_maximo(parametro):
    # return max(parametro)
    g = 0
    for i in parametro:
        if i > g:
            g = i
    return g
# print(encontrar_maximo(numeros))

#-----------------------------------------
def es_multiplo(a,b):
    if a % b == 0:
        x = True
    else:
        x = False
    return x
# print(es_multiplo(4,3))
# ----------------------------------------------
# 16)Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
#  Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y 
# mínima de cada día y vaya mostrando la media.El programa pedirá el número de días que se van a introducir.

def temper_media(maxi,mini):
    return (maxi + mini)/2
# print(temper_media(39.2,26.4))

def temperatura_diaria(dias_total):
    
    for i in range(1,dias_total+1):
        print(f'A continuacion ingrese temperatura maxima y minima del dia: {i}')
        maxi = float(input('Ingrese temperatura maxima del dia:'))
        mini = float(input('Ingrese temperatura minima del dia:'))
        x = round(temper_media(maxi,mini),2)
        print(f'La temperatura media del dia {i} es {x} grados')
        print()
    return

# temperatura_diaria(2)

#-----------------------------------------------

# 17)Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
# cadena con un espacio adicional tras cada letra.
#  Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use
# dicha función.

def convertir_espaciado(texto):
    salida = ''
    for i in texto:
        salida += i + ' '
    return salida
# print(convertir_espaciado('hola,chau'))

#--------------------------------------------

# 19)Diseñar una función que calcule el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y 
# muestre su área y perímetro.

def calculo_circulo(radio):
    pi = 3.14
    area = pi*(radio)**2
    perimetro = 2*(pi)*radio
    return print(f'El area del radio dado es:{area} y su perimetro es {perimetro}')
# calculo_circulo(4)

#-------------------------------------------

# Escribir dos funciones que permitan calcular:
#  La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#  La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#  Escribe un programa principal con un menú donde se pueda elegir la opción de convertir
# a segundos, convertir a horas,minutos y segundos o salir del programa.

def cant_segundos(horas,minutos,segundos):
    h = horas * 3600
    m = minutos * 60
    return h + m + segundos

# print(cant_segundos(127,458,54))

def cantidad_horas(segundos):
    horas = segundos//3600
    resto_horas = segundos % 3600
    minutos = 0
    seg_salida = 0
    if resto_horas >= 60:
        minutos += resto_horas // 60
        seg_salida += resto_horas % 60
    else:
        seg_salida += resto_horas
    return print(f'Total {horas} horas, {minutos} minutos, {seg_salida} segundos')

# cantidad_horas(458888)

def convertir_tiempo():

    while True:

        print()
        print('>>> MENU <<<')
        print('Seleccione una opcion para convertir tiempo: ')
        print('Que desea hacer ? ')
        print('Opcion .1 Convierte horas, minutos y segundos a total de segundos')
        print('Opcion .2 Convierte segundos a horas, minutos y segundos')
        print('Opcion .3 Salir')
        print()
        opcion = int(input('Ingrese una opcion: '))
        print()

        if opcion == 1:
            hora = int(input('ingrese cantidad en horas: '))
            minutos = int(input('ingrese cantidad en minutos: '))
            segundos = int(input('ingrese cantidad en segundos: '))
            print()
            print(f'El Total es de: {cant_segundos(hora,minutos,segundos)} segundos')
        elif opcion == 2:
            segund = int(input('Ingrese la cantidad de segundos a tranformar: '))
            print()
            cantidad_horas(segund)
            print()
        elif opcion == 3:
            break

# convertir_tiempo()

#----------------------------------------------------------------
# Crear una funcion que dado un número genere una sucesión de fibonacci con esa cantidad
# de números en la sucesion, por ejemplo: 3 -> 0,1,1 o 5 -> 0,1,1,2,3

def fibonacci(n):
    x = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        for _ in range(n - 2):
            x.append(x[-1] + x[-2])
    return x

# print(fibonacci(5))

#--------------------------------------------------------


def collatz(n):
    salida = []
    salida.append(int(n))
    while salida[-1] > 1:
        if salida[-1] % 2 == 0:
            salida.append(int(salida[-1]/2))
        else: 
            salida.append(int((3*(salida[-1]))+1))
    return salida

# print(collatz(5))

def impresion_collatz(n):
    print('n =',n)
    for i in range(1,n+1):
        w = (collatz(i))
        print(i,len(w)*'*')
    return
# impresion_collatz(20)




#--------------------------------------------------------------


from datetime import *

# fecha_hoy = datetime.now()
# nacimiento = datetime(year=1984, month=2, day=2)
# tiempo = fecha_hoy - nacimiento
# print(tiempo)




# # # # # modulo Random

from random import *

# def quini_random(): 
#     for _ in range(6):
#         print(randint(0,45)) # quini 6
# quini_random()

lista = ["hola", "adios", "buen dia", "buenas tardes"]

cadena_aleatoria = choice(lista)
# print(cadena_aleatoria)

caracteres = "asdqwertptoyiuÃ±lkjhcvmnx123456789!#$?"
clave = ""
for i in range(8):
    clave_aleatoria = choice(caracteres)
    clave += clave_aleatoria

# print(clave)
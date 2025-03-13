class Humano:
    """clase persona"""

    def __init__(self,nacimiento,edad,padres,genero,peso,altura,color_de_pelo,color_de_ojos):
        self.nacimiento = nacimiento
        self.edad = edad
        self.padres = padres
        self.genero = genero
        self.peso = peso
        self.altura = altura
        self.color_de_pelo = color_de_pelo
        self.color_de_ojos = color_de_ojos

    def get_edad(self):  # metodo para asegurar el atributo de edad
        return self.edad

    def correr(self):
        print('esta corriendo')
    
    def caminar(self):
        print('empieza a caminar')

    def hablar(self):
        print('Hablando')

Marcos = Humano('24/3/93',26,'Rosa, Leonardo','M', 69, 1.74,'rubio','verdes')
Elisa = Humano('24/3/92',27,'Antonia, Martin','F', 67, 1.64, 'Negro', 'Cafe')

# print(Marcos.edad)
# print(Marcos.get_edad())

instancias = [Marcos,Elisa]
# print(Humano.__dict__)


# for clave, valor in (Marcos.__dict__).items():
#     print(clave,': ', valor)
# print()
# for clave, valor in (Elisa.__dict__).items():
#     print(clave,': ', valor)

# for elementos in Marcos.__dict__.items():
#     print(elementos)

## --------------------------------------------------

# ga = Marcos.__dict__
# for i in ga:
#     if ga[i] == 26:
#         del ga[i]      Da error , no se puede usar del en iteracion de diccionario

## -----------------------------------------------------

b = {}
a = Marcos.__dict__
for i in a.keys() - {'altura'}:
    b[i] = a[i]
# print(b)
claves = []
valores = []
for clave , valor in Marcos.__dict__.items():
    claves.append(clave)
    valores.append(valor)
# print(claves,valores)
volver= dict((zip(claves,valores)))
# print(volver)
# print(dir(Marcos))
# print(dir(Humano))
# # --------------------------

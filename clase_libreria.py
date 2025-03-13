class Libro():

    def __init__(self, titulo, autor, isbn, numero_de_paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.___paginas = numero_de_paginas
        self.genero = genero
        self.prestado = False

    def get__paginas(self):
        return self.___paginas

    def prestar(self):
        self.prestado = True

    def devolver(self):
        self.prestado = False

    def buscar_por_titulo(self):
        print(
            f'El libro {self.titulo}, tiene in ISBN {self.isbn}, y un total de {self.___paginas} paginas'
        )


class Autor():

    def __init__(self, nombre, nacionalidad, fecha_nac):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nac = fecha_nac

    def libro_publicado(self, param: Libro):
        if param.autor == self.nombre:
            print(f'{self.nombre} publico el libro: {param.titulo}')
        else:
            print(f'el autor {self.nombre} no publico este libro')


class Lector:
    # Constructor inicializo los atributos
    def __init__(self, nombre, edad, direccion, numero_socio):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numero_socio = numero_socio

    def solicitar_prestamo(self, libro):
        print(
            f"{self.nombre} ha solicitado el préstamo del libro '{libro.titulo}'."
        )

    def devolver_libro(self, libro):
        print(f"{self.nombre} devuelve el libro '{libro.titulo}'.")


class Libreria():

    def __init__(self):

        self.libros = []
        self.autor = []
        self.lector = []

    def agregar_libro(self, param: Libro):
        self.libros.append(param)

    def registrar_lector(self, lector_nuevo):
        self.lector.append(lector_nuevo)

    def prestar_libro(self, param: Libro):
        if param in self.libros:
            i = self.libros.index(param)
            if self.libros[
                    i].prestado:  # llama al atributo de control de libro
                print(
                    'el libro esta prestado, no se encuentra disponible por el momento'
                )
            else:
                self.libros[i].prestar()  # metodo de libro
                print(
                    f'se le esta prestando el libro: {self.libros[i].titulo}')
        else:
            print('el libro no esta en la libreria')

    def buscar_libro(self, param: Libro):
        if param in self.libros:
            i = self.libros.index(param)
            print(
                f'el libro: {self.libros[i].titulo}, pertenece al genero: {self.libros[i].genero}'
            )
            print(
                f'tiene un total de {self.libros[i].get__paginas()} paginas, {self.libros[i].autor} es su autor'
            )
            if self.libros[i].prestado:
                print('lamentablemente se encuentra prestado')
            else:
                print('actualmente se encuentra disponible para ser leido')

    def devolver_libro(self, param: Libro, paramm: Lector):
        print(f' Hola  {paramm.nombre} bienvenido')
        print(f'Estas devolviendo el libro:{param.titulo}. Muchas gracias')
        param.devolver()


lectorrr = Lector('roberto', 55, 'lapampa', 4545)
pr = Libro('principito', 'pedro', 4, 195, 'infantil')
pr_a = Autor('pedro', 'uruguay', 22 / 10 / 59)
matrix = Libreria()

# matrix.agregar_libro(pr)
# matrix.buscar_libro(pr)
# matrix.prestar_libro(pr)
# matrix.buscar_libro(pr)
# matrix.devolver_libro(pr, lectorrr)
# # print(matrix.lector)
# matrix.registrar_lector(lectorrr)
# # print(matrix.lector)

# pollo = Libro('p', 'e', 4, 18, 'ii')
# matrix.agregar_libro(pollo)
# matrix.prestar_libro(pollo)
# lectorrr.solicitar_prestamo(pr)
# lectorrr.devolver_libro(pr)
# pr_a.libro_publicado(pr)
# pr_a.libro_publicado(pollo)
# pollo.buscar_por_titulo()

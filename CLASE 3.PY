
# EJERCICIO 2:
# Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
# constructor que recibe ambos valores.
# ● Definir métodos tales como:
# ○ eje_x
# ○ eje_y
# ○ impresion (método que devuelve en representación de string ambos valores)
# ○ opuesto (método que devuelve el punto opuesto -es decir con los atributos
# negativos-)

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def eje_x(self) -> float:
        return self.x

    def eje_y(self) -> float:
        return self.y

    def impresion(self) -> str:
        return f"({self.x}, {self.y})"

    def opuesto(self) -> object:
        return Punto(-self.x, -self.y)


# EJERCICIO 3

# Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
# pasa la línea en un espacio de dos dimensiones.
# La clase dispondrá de los siguientes métodos:
# ● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
# Punto, que son utilizados para inicializar los atributos.
# ● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
# ● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
# ● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
# ● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.



class Linea:
    def __init__(self, punto_a: object, punto_b: object):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia: float):
        self._punto_a.x += distancia
        self._punto_b.x += distancia

    def mueve_izquierda(self, distancia: float):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia

    def mueve_arriba(self, distancia: float):
        self._punto_a.y += distancia
        self._punto_b.y += distancia

    def mueve_abajo(self, distancia: float):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia

    def impresion(self) -> str:
        return f"Linea de A{self._punto_a.impresion()} a B{self._punto_b.impresion()}"
    


# EJERCICIO 4

# Desarrolla una clase Cancion con los siguientes atributos:
# ● titulo: una variable String que guarda el título de la canción.
# ● autor: una variable String que guarda el autor de la canción.
# Con los siguientes métodos:
# ● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
# canción (por este orden).
# ● get_titulo(): devuelve el título de la canción.
# ● get_autor(): devuelve el autor de la canción.
# ● set_titulo(String): establece el título de la canción.
# ● set_autor(String): establece el autor de la canción

class Cancion:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self) -> str:
        return self.titulo

    def get_autor(self) -> str:
        return self.autor

    def set_titulo(self, nuevo_titulo: str):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor: str):
        self.autor = nuevo_autor




# EJERCICIO 5

# Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
# cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
# (ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
# servicios: getters y setters, método para leer la información y método para mostrar la
# información.
# ● Este último método mostrará la información del libro con este formato:
# Título: Introduction to Java Programming 3a. edición
# Autor: Liang, Y. Daniel
# ISBN: 0-13-031997-X
# Prentice-Hall, New Jersey (USA)
# viernes 16 de noviembre de 2001
# 784 páginas


class Persona:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def get_nombre(self) -> str:
        return self.nombre

    def get_apellido(self) -> str:
        return self.apellido

    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre

    def set_apellido(self, apellido: str) -> None:
        self.apellido = apellido

    def impresion(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, paginas: int, edicion: str, editorial: str, lugar: str, fecha_edicion: int) -> None:
        self.titulo = titulo
        self.autor = autor  
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar  
        self.fecha_edicion = fecha_edicion

    def get_titulo(self) -> str:
        return self.titulo
    
    def get_autor(self) -> str:
        return self.autor
    
    def get_isbn(self) -> str:
        return self.isbn
    
    def get_paginas(self) -> int:
        return self.paginas
    
    def get_edicion(self) -> str:
        return self.edicion
    
    def get_editorial(self) -> str:
        return self.editorial
    
    def get_lugar(self) -> str:
        return self.lugar
    
    def get_fecha_edicion(self) -> int:
        return self.fecha_edicion

    def set_titulo(self, titulo) -> None:
        self.titulo = titulo

    def set_autor(self, autor) -> None:
        self.autor = autor

    def set_isbn(self, isbn) -> None:
        self.isbn = isbn

    def set_paginas(self, paginas: int) -> None:
        self.paginas = paginas

    def set_edicion(self, edicion: str) -> None:
        self.edicion = edicion

    def set_editorial(self, editorial: str) -> None:
        self.editorial = editorial

    def set_lugar(self, lugar: str) -> None:
        self.lugar = lugar

    def set_fecha_edicion(self, fecha_edicion: int) -> None:
        self.fecha_edicion = fecha_edicion

    def mostrar_informacion(self):
        autor_completo = self.autor.impresion()
        ciudad, pais = self.lugar
        return (f"Título: {self.titulo} {self.edicion} edición\n"
                f"Autor: {autor_completo}\n"
                f"ISBN: {self.isbn}\n"
                f"{self.editorial}, {ciudad} ({pais})\n"
                f"{self.fecha_edicion}\n"
                f"{self.paginas} páginas")






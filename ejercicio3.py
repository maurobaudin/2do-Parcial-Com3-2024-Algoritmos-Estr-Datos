class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.nombre = nombre
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.carrera = carrera

    def __str__(self):
        return f"Alumno(nombre='{self.nombre}', DNI={self.dni}, " \
               f"FechaIngreso={self.fecha_ingreso}, Carrera='{self.carrera}')"

# Definición de la clase Nodo para la lista doblemente enlazada
class Nodo:
    def __init__(self, alumno=None):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

# Definición de la clase ListaDoblementeEnlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def esta_vacia(self):
        return self.size == 0

    def insertar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.size += 1

    def lista_ejemplo(self, cantidad):
        for _ in range(cantidad):
            nombre = f"Alumno{random.randint(1, 100)}"
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = random.randint(2010, 2023)  # Año aleatorio entre 2010 y 2023
            carrera = random.choice(["Ingeniería Informática", "Medicina", "Derecho", "Arquitectura"])
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.insertar_al_final(alumno)

    def __iter__(self):
        self._iterador_actual = self.cabeza
        return self

    def __next__(self):
        if self._iterador_actual is None:
            raise StopIteration
        else:
            alumno = self._iterador_actual.alumno
            self._iterador_actual = self._iterador_actual.siguiente
            return alumno


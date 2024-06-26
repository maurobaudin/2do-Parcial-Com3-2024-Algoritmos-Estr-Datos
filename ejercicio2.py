from datetime import datetime

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

    def cambiar_datos(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.datos:
                self.datos[key] = value
            else:
                print(f"Atributo '{key}' no válido para Alumno.")

    def antiguedad(self):
        fecha_ingreso = self.datos["FechaIngreso"]
        hoy = datetime.now()
        diferencia = hoy - fecha_ingreso
        return diferencia.days  # devuelve la cantidad de días desde la fecha de ingreso

    def __str__(self):
        return f"Alumno(nombre={self.datos['Nombre']}, DNI={self.datos['DNI']}, " \
               f"FechaIngreso={self.datos['FechaIngreso']}, Carrera={self.datos['Carrera']})"

    def __eq__(self, other):
        return self.datos == other.datos

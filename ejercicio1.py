class Fecha:
    def _init_(self, dd=None, mm=None, aaaa=None):
        if dd is None or mm is None or aaaa is None:
            # Si no se proporcionan los parámetros, tomar la fecha de hoy
            today = date.today()
            self.dd = today.day
            self.mm = today.month
            self.aaaa = today.year
        else:
            self.dd = dd
            self.mm = mm
            self.aaaa = aaaa

    def calcular_dif_fecha(self, otra_fecha):
        # Calcular la diferencia entre dos fechas
        fecha1 = date(self.aaaa, self.mm, self.dd)
        fecha2 = date(otra_fecha.aaaa, otra_fecha.mm, otra_fecha.dd)
        diferencia = abs(fecha1 - fecha2).days
        return diferencia

    def _str_(self):
        # Sobrecarga del método str para imprimir la fecha en formato (dd, mm, aaaa)
        return f"({self.dd}, {self.mm}, {self.aaaa})"

    def _add_(self, dias):
        # Sobrecarga del operador de suma para sumar días a la fecha actual
        fecha_actual = date(self.aaaa, self.mm, self.dd)
        nueva_fecha = fecha_actual + timedelta(days=dias)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def _eq_(self, otra_fecha):
        # Sobrecarga del operador de igualdad para comparar si dos fechas son iguales
        return (self.dd == otra_fecha.dd and
                self.mm == otra_fecha.mm and
                self.aaaa == otra_fecha.aaaa)

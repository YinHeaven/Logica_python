#Herencia y polimorfismo ejemplo de: gerarquia de una empresa

# Clase madre
class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def mostrar_informacion(self):
        return f"ID: {self.id}, Nombre: {self.nombre}"

# Subclase Gerente
class Gerente(Empleado):
    def __init__(self, id, nombre, departamento):
        super().__init__(id, nombre)
        self.departamento = departamento
        self.trabajadores = []  # Lista para almacenar trabajadores a cargo

    def agregar_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)

    def mostrar_informacion(self):
        trabajadores_info = ", ".join([
            trabajador.nombre 
            for trabajador in self.trabajadores
            ]) or "Sin trabajadores a cargo"
        return f"{super().mostrar_informacion()}, Departamento: {self.departamento}, Trabajadores a cargo: {trabajadores_info}"

# Subclase Encargado
class Encargado(Empleado):
    def __init__(self, id, nombre, area):
        super().__init__(id, nombre)
        self.area = area

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Área: {self.area}"

# Subclase Trabajador
class Trabajador(Empleado):
    def __init__(self, id, nombre, turno):
        super().__init__(id, nombre)
        self.turno = turno

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Turno: {self.turno}"

# Ejemplo de uso
gerente = Gerente(1, "Juan", "Ventas")
encargado = Encargado(2, "María", "Producción")
trabajador1 = Trabajador(3, "Carlos", "Nocturno")
trabajador2 = Trabajador(4, "Ana", "Diurno")

# Agregar trabajadores al gerente
gerente.agregar_trabajador(trabajador1)
gerente.agregar_trabajador(trabajador2)

# Mostrar información
print(gerente.mostrar_informacion())
print(encargado.mostrar_informacion())
print(trabajador1.mostrar_informacion())
print(trabajador2.mostrar_informacion())

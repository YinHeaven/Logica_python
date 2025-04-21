

#funciones y alcance de variables


#funcion simple 


def  saludo():
    print("Hola Mundo")

saludo()

#funcion con retorno
def saludo(nombre):
    return "Hola " + nombre

saludo = saludo("Juan")
print(saludo)


#funcion con argumentos
def saludo(nombre, apellido):
    print(f"Hola {nombre} {apellido}")

saludo("Juan", "Lopez")
#or
saludo(nomre="Juan", apellido="Lopez")
 
#funcion con argumento por defecto
def saludo(nombre, apellido="Lopez"):
    print(f"Hola {nombre} {apellido}")

saludo("Juan") 

#funcion con numeros de argumentos variables

def saludo(*nombres):
    for nombre in nombres:
        print(f"Hola {nombre}")

saludo("Juan", "Pedro", "Maria") #saluda a todos por separado

#funcion con argumentos de palabra clave variables
def saludo(**nombres):
    for nombre, apellido in nombres.items():
        print(f"Hola {nombre} {apellido}")

saludo(Juan="Lopez", Pedro="Gonzalez", Maria="Fernandez") #saluda a todos por separado

#funcion lambda 
def saludo(nombre):
    return lambda apellido: f"Hola {nombre} {apellido}"

#funncion dentro de una funcion
def saludo(nombre):
    def saludo_apellido(apellido):
        return f"Hola {nombre} {apellido}"
    return saludo_apellido







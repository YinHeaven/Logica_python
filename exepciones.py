#Exepciones

try:
    print(10/1)
    print([1,2,3,4][4])
except Exception as e:
    print(f"Se ha producido un error: {e}") # la excepcion capturada se llama e y en el print se interpola dicha variable

    print(f"Error: {e} ({type(e).__name__}) \n\n\n ")  # lo mismo pero aqui busco el tipo de error e imprimo


# ejercicio de control de expeciones tambien se puede  crear exepciones

class stringError(Exception): #con esto se hereda la  funcionalidad de las excepciones y se crea un nuevo error
    pass

def parametro(parametro: list):
    """Función que lanza excepciones según las condiciones de la lista."""
    if len(parametro) > 3:
        raise IndexError("La lista tiene más de 3 elementos.")
    elif parametro[1] == 0:
        raise ZeroDivisionError("El segundo elemento de la lista es 0.")
    elif type(parametro[2]) == str:
        raise stringError("El tercer elemento de la lista es una cadena de texto.")
    
    print(parametro[2])
    print(parametro[0] / parametro[1])
    print(parametro[2] + 3)

# Ejemplos para cada excepción
try:
    print("Ejemplo 1: Lanzando IndexError")
    parametro([1, 2, 3, 4])  # Más de 3 elementos
except IndexError as a:
    print(f"IndexError: {a}")

try:
    print("\nEjemplo 2: Lanzando ZeroDivisionError")
    parametro([1, 0, 3])  # Segundo elemento es 0
except ZeroDivisionError as b:
    print(f"ZeroDivisionError: {b}")

try:
    print("\nEjemplo 3: Lanzando stringError")
    parametro([1, 2, "3"])  # Tercer elemento es una cadena
except stringError as c:
    print(f"stringError: {c}")

try:
    print("\nEjemplo 4: Sin errores")
    parametro([4, 2, 3])  # Lista válida
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Ningún error encontrado.")

finally:
    print("\nEl programa no se ha bloqueado.") #finally siempre se va a ejecutar independientemente si se produce o no un er

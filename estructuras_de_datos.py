
#ESTRUCTURAS DE DATOS (son contenedores de datos)
# 1. Listas (son mutables)
#1. Listas
my_set = [1, 2, 3, 4, 5]
my_set.append(6)  # Agrega el elemento 6 al conjunto
my_set.discard(3)  # Elimina el elemento 3 del conjunto
my_set.remove(2)  # Elimina el elemento 2 del conjunto
print(my_set)  # Imprime el conjunto actualizado
my_set[0]  # Accede al primer elemento del conjunto (esto no es válido para conjuntos, ya que no tienen un orden específico)
my_set[0] = 10  # Esto no es válido, ya que los conjuntos son inmutables
my_set.sort()  # Esto no es válido, ya que los conjuntos no tienen un orden específico

#2. Tuplas (son inmutables) (almacena grandes conjuntos de datos)
my_tuple = (1, 2, 3, 4, 5)
my_tuple[0]  # Accede al primer elemento de la tupla
my_tuple[0] = 10  # Esto no es válido, ya que las tuplas son inmutables
my_tuple.sort()  # Esto no es válido, ya que las tuplas no tienen un método sort()
my_tuple.append(6)  # Esto no es válido, ya que las tuplas no tienen un método append()
my_tuple.remove(2)  # Esto no es válido, ya que las tuplas no tienen un método remove()
my_tuple.pop(0)  # Esto no es válido, ya que las tuplas no tienen un método pop()


#3. Conjuntos
#4. Diccionarios (son mutables) (alamacena grandes conjuntos de datos)
my_dict = {"key1": "value1", "key2": "value2"}
my_dict["key3"] = "value3"  # Agrega una nueva clave y valor al diccionario
my_dict["key1"] = "new_value"  # Cambia el valor de la clave "key1"
my_dict.pop("key2")  # Elimina la clave "key2" del diccionario
my_dict.clear()  # Limpia el diccionario, eliminando todas las claves y valores
print(my_dict)  # Imprime el diccionario vacío


#5. Pilas
#6. Colas
#7. Arboles
#8. 

#creame una lista, una tupla y un diccionario

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_dict = {"key1": "value1", "key2": "value2"}
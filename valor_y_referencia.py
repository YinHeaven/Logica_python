# valor y referencia

#tipos de datos por valor (copia el valor)


entero_a = 10
entero_b = entero_a
entero_b = 20
print(entero_a) #10
print(entero_b) #20

#tipos de datos por  referencia (hereda la posicion de memoria)
lista_a = [1,2,3]
lista_b = lista_a
lista_b[0] = 10
print(lista_a) #10,2,3

lista_b.append(4)
print(lista_a) #10,2,3,4
print(lista_b) #10,2,3,4

#funciones con datosp or valor
entero_c = 10

def cambiar_valor(valor):
    valor = 20
    return valor
cambiar_valor(entero_c)
print(entero_c) #10

#funciones con datos por referencia

def cambiar_referencia(lista):
    lista_c;append(4)
    return 

lista_c = [1,2,3]
cambiar_referencia(lista_c)
print(lista_c) #1,2,3,4

#ejemplo de funciones con datos por valor

entero_d = 10
entero_e = 20

def value(valor_a: int, valor_b: int) -> tuple:
    temp = valor_a
    valor_a = valor_b
    valor_b = temp
    return valor_a, valor_b

# Reasignar los valores retornados
entero_f, entero_g = value(entero_d, entero_e)

print(f"entero_d: {entero_d}, entero_e: {entero_e}") #20,10
print(f"entero_d: {entero_f}, entero_e: {entero_g}") #20,10

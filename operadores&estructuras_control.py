#operadores aritmeticos

print(f"suma= {2+2}")
print(f"resta= {2-2}")
print(f"multiplicacion= {2*2}")
print(f"division= {2/2}")
print(f"division entera= {2//2}")
print(f"modulo= {2%2}")
print(f"potencia= {2**2}")
print(f"raiz= {2**(1/2)}")
print(f"raiz= {2**0.5}")

#operadores de comparacion
print(f"igual= {2==2}")
print(f"distinto= {2!=2}")
print(f"mayor= {2>2}")
print(f"menor= {2<2}")
print(f"mayor o igual= {2>=2}")
print(f"menor o igual= {2<=2}")

#operadores logicos
print(f"and &&= {True and False}")
print(f"or ||= {True or False}")
print(f"not != {not True}")
print(f"xor= {True ^ False}")

#operadores de identidad
print(f"es= {2 is 2}")
print(f"no es= {2 is not 2}")
print(f"es= {2 is 2.0}")
print(f"no es= {2 is not 2.0}")

#operadores de logicos
print(f"and= {True and False}")
print(f"or= {True or False}")
print(f"not= {not True}")

#operadores de pertenencia
print(f"en= {2 in [1,2,3]}")
print(f"no en= {2 not in [1,2,3]}")

#operadores de asignacion
numero = 2

#suma y asignacion
nuemro += 2

#resta y asignacion
numero -= 2

#multiplicacion y asignacion
numero *= 2

#division y asignacion
numero /= 2

#division entera y asignacion
numero //= 2

#modulo y asignacion
numero %= 2

#potencia y asignacion
numero **= 2


#estructuras de contrtol

#estructura de control if (condicional)
numero = 2
if numero == 2:
    print("es 2")
elif numero == 3:
    print("es 3")
else:
    print("no es 2 ni 3")

#estructura de control iteractivas (for, while)
#estructura de control for
for i in range(10):
    print(i)   

#estructura de control while
numero = 0
while numero < 10:
    print(numero)
    numero += 1

#menojo de excepciones
#try except
try:
    numero = int(input("ingrese un numero: "))
except ValueError:
    print("no es un numero")
except ZeroDivisionError:
    print("division entre cero")
except Exception as e:
    print(f"error: {e}")
finally:
    print("fin del programa")





#cadena de caracteres

#operaciones
s1 = "Hola"
s2 = " Mundo"

#concatenacion
print(s1 + s2) #Hola Mundo
print(s1 + " " + s2 "!") #Hola Mundo!

#repeticion
print(s1 * 3) #HolaHolaHola

#indexacion
print(s1[0]) #H
print(s1[1]) #o
print(s1[2]) #l
print(s1[3]) #a

print(s1[0]+s1[1]+s1[2]+s1[3]) #Hola

#slicing
print(s1[0:2]) #Ho
print(s1[0:3]) #Hol
print(s1[0:4]) #Hola
print(s1[0:]) #Hola
print(s1[:]) #Hola

#busqueda
print(s1.find("H")) #0
print(s1.find("o")) #1

#busqueda buleano
print("H" in s1) #True
print("H" not in s1) #False

import sys

print(sys.version)
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

print("Frankly Poveda", "Colombia", "Estoy disfrutando 30 dias de Python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(["asabeneh", "Python", "Finland"]))
print("Frankly")
print("Poveda")
print("Colombia")

#Nivel 3

#Entero
print("Esto es un entero.")
print(100)

#Float
print("Esto es un Float.")
print(3.53)

#Comlejo
print("Esto es un complejo.")
print(3+6j)

#Cadena
print("Esto es un cadena.")
print("Hola")

#Booleano
print("Esto es un booleano.")
print("True or False")

#Lista
print("Esto es un lista.")
print(["hola", "equisde"])

#Tuple
print("Esto es un tupla")
print(("hola", "equisde"))

#Set
print("Esto es un set.")
print({"hola", "equisde"})

#Diccionario
print("Esto es un diccionario.")
print({"hola":"equisde", "prueba":"esta"})

#Distancia euclidana entre (2,3) y (10,8)
A = (2,3)
B = (10,8)
C = (B[0]-A[0], B[1]-A[1])
print(((C[0])**2 + (C[1])**2)**0.5)
print(C)
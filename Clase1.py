"""Actividad 3"""

# print ("Hello World")

"""Actividad 4"""

# edad=19
# altura=1.7
# nombre="Daniel"
# mascota= True
# carros =["BMW","Ford","KIA"]

# print (f'Nombre: {nombre}\nEdad: {edad} anos\nAltura: {altura} \nMascota: {mascota}\nCarros: {carros}')

"""Actividad 5"""

# Edad = 5

# if (Edad > 18):
#     print ("Eres mayor de edad")
# else:
#     print ("Eres menor de edad")

"""Actividad 6"""


# def Resultado (Edad):

#     if (Edad >= 18):
#         return True
#     else:
#         return False

# Edad = 18

# print("Edad del usuario ",Edad)
# Final = Resultado (Edad)
# print (Final)

"""ACTIVIDAD"""
"""Nivel basico"""
#1
# Num = int(input("Digita tu numero"))

# if (Num < 0):
#     print ("El numero es Positivo")
# elif (Num == 0):
#     print ("El numero es Negativo")
# else:
#     print ("El numero es Cero")

#2
# Calificacion = int(input("Digita tu calificacion"))

# if (Calificacion < 30):
#     print ("Lo siento NO APROBASTE")
# else:
#     print ("!!APROBADO!!")

"""Nivel intermedio"""

#1
# Num = int(input("Digita tu numero"))

# if Num % 2 == 0:
#     print("El Numero es par")
# else:
#     print("El numero es impar") 

#2
# Num = int(input("Digita tu numero"))

# if Num >=1 and Num <= 10:
#     print("El numero esta en el rango de 1 a 10")
# else:
#     print("El numero no esta en el rango de 1 a 10") 

"""Nivel avanzado"""

#1
# peso = int(input("Digita el peso del paquete"))
# destino = input("si envio es internaciona? (si/no)")
# valor=0

# if (peso < 1):
#     valor=5
# elif (peso >= 1 and peso <= 5):
#     valor=10
# elif (peso > 5):
#     valor=20
# else:
#     print ("El peso que ingreso es invalido")

# if valor > 0:
#     if (destino == "si"):
#         valor = valor + (valor/2)
#         print ("Su envio Internacional tiene una valor de : ",valor)
#     if (destino == "no"):
#         print ("Su envio Nacional tiene una valor de : ",valor)
#     else:
#         print ("el valor de destino no es correcto porfavor digite si o no")
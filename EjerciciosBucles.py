# 1) Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input("Introdusca una palabra: ")
for i in range(10):
  print(palabra)
  
# 2) Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
 
edad = int(input("Ingresa tu edad: "))
for i in range(edad):
  print(i+1)

# 3) Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Ingrese un numero entero positivo: "))

for i in range(numero):
  i=i+1
  if i%2 == 1:
    print(i, end=", ")
    
# 4) Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Ingrese un numero entero positivo: "))

for i in range(numero,0,-1):
  print(i)

# 5) Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la 
inversión cada año que dura la inversión.

inversion = int(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual: "))
anios = int(input("Ingrese la cantidad de años: "))

for i in range(anios):
  print(inversion*interes_anual * ( i + 1 ))
  
# 6) Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido. 
 
numero = int(input("Ingrese un numero: "))

for i in range(numero):
  i = i + 1
  print("*" * i)

# 7) Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(10):
  i = i + 1
  print("\n")
  for k in range(10):
    k = k + 1
    print(i * k, end=" ")

# 8) Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
'''
1

3 1

5 3 1

7 5 3 1

9 7 5 3 1 '''

numero = int(input("Ingrese un numero entero positivo: "))

for i in range(numero):
  i = i + 1
  if i % 2 == 1:
    print(i)

# 9) Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
correcta.

password = "contraseña"

psswrd = input("Ingrese la contraseña: ")

while password != psswrd:
  psswrd = input("Contraseña incorrecta, vuelva a introducirla: ")

print("\nBienvenido al Sistema.")

# 10) Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero = int(input("Ingrese un numero entero positivo: "))
cant=0
for i in range(1,numero+1):
  if numero%i == 0:
    cant = cant+1
if(cant == 2):
  print("Es un numero primo.")
else:
  print("No es un numero primo")
  
# 11) Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Ingrese una palabra: ")

for i in range(len(palabra), 0, -1):
  print(palabra[i-1])

# 12) Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
cant=0
for i in frase:
  if i == letra:
    cant += 1
print(f"\nLa letra {letra} aparece {cant} veces")

# 13) Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

palabra = input("Ingrese una palabra: ")

while palabra != "salir":
  print(palabra)
  palabra = input("Ingrese una palabra: ")
  
  

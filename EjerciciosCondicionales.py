# 1) Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
  print("Usted es mayor de edad.")
else:
  print("Usted no es mayor de edad.")
  
# 2) Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
# introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

pwd = "contraseña"

palabra = input("Ingrese la contraseña: ").lower()

if pwd == palabra:
  print("La contraseña coincide con la guardada.")
else:
  print("La contraseña no coincide.")

# 3) Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

if divisor == 0:
  print("Error!")
else:
  print(dividendo /divisor)

# 4) Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Ingrese un numero: "))

if numero%2 == 0:
  print("\nNumero PAR.")
else: 
  print("\nNumero IMPAR")

# 5) Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que
# pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Ingrese su edad: "))
ingresos = int(input("Sueldo mensual: "))

if edad >= 16 and ingresos >= 1000:
  print("Usted reune los requisitos para tributar.")
else:
  print("Usted no reune los requisitos para trbutar.")


# 6) Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a 
# la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

sexo = input('Ingrese su sexo (F/M): ').upper()
nombre = input('Ingrese su nombre: ').upper()

if nombre[0] <= 'M' and sexo == 'F' or nombre[0] >= 'N' and sexo == 'M':
  print("Perteneces al grupo A!")
else:
  print('Perteneces al grupo B!')

  
# 7) Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#       Renta           ||   Tipo impositivo
# Menos de 10000€       ||       5%
# Entre 10000€ y 20000€ ||       15%
# Entre 20000€ y 35000€ ||       20%
# Entre 35000€ y 60000€ ||       30%
# Más de 60000€         ||       45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

print("Cálculo de Tipo Impositivo\n")
renta = float(input("Ingrese su renta anual: "))
print('\n')
if renta < 10000:
  print(f'El tipo Impositivo que le corresponde es de 5% ')
elif renta >= 10000 and renta < 20000:
  print(f'El tipo Impositivo que le corresponde es de 15% ')
elif renta >= 20000 and renta < 35000:
  print(f'El tipo Impositivo que le corresponde es de 20% ')
elif renta >= 35000 and renta < 60000:
  print(f'El tipo Impositivo que le corresponde es de 30% ')
else: 
  print(f'El tipo Impositivo que le corresponde es de 45% ')
  
 
# 8) En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir 
# aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las 
# cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€
# multiplicada por la puntuación del nivel.

#   Nivel     || Puntuación
# Inaceptable ||   0.0
# Aceptable   ||   0.4
# Meritorio   ||   0.6 o más



# 9) Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus 
# clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar
# gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input('Ingrese su edad por favor: '))
print('\n')
if edad < 4:
  print('Entrada Gratuita!')
elif edad >=4 and edad < 18:
  print('Valor Entrada 5€')
else :
  print('Valor Entrada 10€')
  
# 10) La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# *Ingredientes vegetarianos: Pimiento y tofu.
# *Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles 
# para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la
# pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print('Quiere Pizza VEGETARIANA?')
opcion = input('si/no: ').lower()

if opcion == 'si':
  print('\nElija un ingrediente')
  ingrediente = input('Pimiento - Tofu: ').lower()
  print(f'\nSu pizza es Vegetariana \n- Ingredientes: Tomate, mozzarella y {ingrediente}')
else:
  print('\nElija un ingrediente')
  ingrediente = input('Peperoni - Jamón - Salmón: ').lower()
  print(f'\nSu pizza no es Vegetariana \n- Ingredientes: Tomate, mozzarella y {ingrediente}')


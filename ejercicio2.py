#Numero se asigna un valor a una variable
numero= 10

#Se imprime el valor de la variable numero, ej. 10
print("El numero asignado es:", numero)

"""
Actividad de clase: Van a definir valores de variables y las van a imprimir; sobre algun hobby
Usaras:
-Enteros
-Booleanos 
-Caracteres
Tiempo: 8 min
"""
# Definición de variables
# Entero: Número de meses entrenando boxeo
meses_entrenando = 10  

# Booleano: Indica si el boxeo es su hobby favorito
es_hobby_favorito = True  

# Caracter: Nivel de dificultad que percibe (A: Alta, M: Media, B: Baja)
nivel_dificultad = 'M'  

# Impresión de valores
print("Tiempo entrenando boxeo:", meses_entrenando, "meses")
print("¿Es el boxeo mi hobby favorito?", es_hobby_favorito)
print("Nivel de dificultad percibido:", nivel_dificultad)

""" Sentencia IF - Es una condicion sentencia """
if numero < 100:
        print("La variable numero es menor que el 100")
"""
Actividad definir 3 tipos de if
-comparacion de un numero contra otro
-ingresar a un lugar con la edad minima 
-sacar la INE
"""
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num1 < num2:
    print("El segundo número es mayor que el primero.")
else:
    print("Ambos numeros son iguales.")


edad = int(input("Ingresa tu edad: "))

if edad <= 18:
    print("Puedes entrar al bar.")
else:
    print("No puedes entrar, eres menor de edad.")

if edad <= 18:
    print("Puedes tramitar tu INE.")
else:
    print("Aún no puedes tramitar tu INE, debes ser mayor de edad.")

"""
   Actividad: Crear 1 IF-ELSE al azar 
""" 
num=int(input("Ingresa un número: "))

if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

""" Investiguen un juego en Python a base de IF-ELSE
Copialo y pegalo aqui 
Comenta cada linea para que interpretes su funcionamiento
"""
import random  # Importamos la librería random para que la computadora elija una opción al azar

# Lista de opciones disponibles en el juego
opciones = ["piedra", "papel", "tijeras"]

# La computadora elige una opción aleatoria
eleccion_computadora = random.choice(opciones)

# El usuario ingresa su elección
eleccion_usuario = input("Elige piedra, papel o tijeras: ").lower()  # Convertimos a minúsculas para evitar errores

# Verificamos si la opción del usuario es válida
if eleccion_usuario not in opciones:
    print("Opción no válida. Debes elegir piedra, papel o tijeras.")

# Si la opción es válida, determinamos el resultado
else:
    print(f"La computadora eligió: {eleccion_computadora}")

    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

print("Hello CodeSandbox!")
print("sebas pelon")
print("miguel burro")
print("naomi bonita")
print("Eduardo")
print("jovanni")
print("levi")
print("keily")
print("cassandra")
print("cerditos")
print("blacky")
""" Vamos a concatenar  """
nombre = "Valeria"
apellido = "Salinas"
print("hola mi nombre es:", nombre)
print("hola mi nombre es:", nombre, apellido) #hola mi nombre es Valeria Salinas
print("hola mi nombre es:", nombre, "y mi apellido es:", apellido) #hola mi nombre es: Valeria y mi apellido es:Salinas

""" Concatenación con diferentes tipos de datos"""
mi_edad=19
mi_nombre="Valeria"
mi_apellido_paterno="Salinas"
mi_apellido_materno="Tejada"
soy_maestra=False
soy_estudiante=True
print("hola mi nombre es:", mi_nombre, "mi apellido paterno es:", mi_apellido_materno, "y mi mi_apellido_materno es:", mi_apellido_materno, "mi edad es:", mi_edad)

""" Uso de type - AAverigua que tipo de dato recibe """
print(type(mi_edad)) #<class 'int'>
print(type(mi_nombre)) #<class 'str'>
print(type(soy_estudiante))#<class 'bool'>

""" operaciones matematicas """
numero_uno=10
numero_dos=10

print(numero_uno+numero_dos) #20
print(numero_uno-numero_dos) #0
print(numero_uno*numero_dos) #100
print(numero_uno/numero_dos) #1.0

#Ask the user to enter the numbers
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number:"))

#Perform operations and display results
print(number_one + number_two)  #Addition
print(number_one - number_two)  #Subtraction
print(number_one * number_two)  #Multiplication
print(number_one / number_two)  #Division
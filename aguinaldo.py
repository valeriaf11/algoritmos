# Calcular el aguinaldo de un trabajador con base en los días trabajados en el año y su salario diario
# Solicitar datos al usuario
salario_diario = float(input("Ingrese su salario diario: "))
dias_trabajados = int(input("Ingrese los días trabajados en el año: "))

# Calcular aguinaldo proporcional
aguinaldo = (15 / 365) * dias_trabajados * salario_diario

# Imprimir el resultado
print(f"El aguinaldo proporcional es: {aguinaldo:.2f}")

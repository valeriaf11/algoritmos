Algoritmo opcionElegida
	Definir numero, a, b Como Entero
	
    Escribir "Elige la opci�n para operar: "
    Escribir "1. Suma"
    Escribir "2. Resta"
    Escribir "3. Multiplicaci�n"
    Escribir "4. Divisi�n"
    Leer numero
	
    Escribir "Ingresa el primer n�mero: "
    Leer a
    Escribir "Ingresa el segundo n�mero: "
    Leer b
	
    Segun numero Hacer
        1:
            Escribir "Resultado: ", a + b
        2:
            Escribir "Resultado: ", a - b
        3:
            Escribir "Resultado: ", a * b
        4:
            Si b <> 0 Entonces
                Escribir "Resultado: ", a / b
            Sino
                Escribir "Error: Divisi�n por cero no permitida"
            FinSi
        De Otro Modo:
            Escribir "No es una opci�n v�lida"
    Fin Segun

FinAlgoritmo

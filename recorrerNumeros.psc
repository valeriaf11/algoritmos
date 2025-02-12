Algoritmo recorrerNumeros
	Definir numero Como entero
	//Pedir al usuario que ingrese un numero del 1 al 3
	Escribir "Dame un numero del 1 al 3"
	Leer numero
	Para i <- 1 Hasta 3 Hacer
		//Verificar si el numero ingresado coincide con el valor i
		Si numero == i Entonces
			Escribir "El numero ingresado es el", i
		Fin Si
	Fin Para
	
FinAlgoritmo

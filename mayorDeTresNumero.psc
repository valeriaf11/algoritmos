Algoritmo mayorDeTresNumero
	//Definir num1, mun2 y num3
	Escribir "Ingresar el primer numero"
	Leer num1
	Escribir "Ingresar el segundo numero"
	Leer num2
	Escribir "Ingresar el tercer numero"
	Leer num3
	//ingresar los numero y verificar cual de los 3 es el mayor
	Si num1 > num2 Y num1 > num3 Entonces 
		numMayor <- num1 
	Sino 
		Si num2 > num1 Y num2 > num3 Entonces 
			numMayor <- num2 
		sino 
			numMayor <- num3
		finsi 
	FinSi
	Escribir " El numero mayor es: ", numMayor
FinAlgoritmo

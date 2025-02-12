Algoritmo cicloFor
	//Estructura de control,que permite ejecutar un numero determinado
	//Definimos las variables
	Definir numero, i Como entero
	
	//Pedir al ususario un numero para comenzar 
	Escribir "Ingrese un numero para empezar su tabla "
	Leer numero
	//Pedir al usuario hasta que numero quiere finalizar
	Escribir "Ingrese hasta que numero quiere parar"
	Leer numfinal
	//Estructura FOR o para en spanish
	Para i<-1 Hasta numfinal Con Paso 1 Hacer
		Escribir "La tabla del " numero, " x " i " = ", numero*i
	Fin Para
FinAlgoritmo

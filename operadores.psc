Algoritmo operadores
	//Vamos a pedir al usuario un numero
	Escribir "Dame un numero del 1 al 10 "
	//Asignar el n�mero de una variable 
	Leer numeroElegido //Eje. 8
	//De acuerdo al n�mero capturado tomamos una decisi�n
	Si numeroElegido >= 1 Y numeroElegido <= 10 Entonces
		//Vamos a hacer comparaciones de n�mero//
		Escribir "Dame un numero a comparar del 1 al 10"
		Leer numeroAComparar //Ej. 5
		Si numeroElegido >= 1 Y numeroAComparar <= 10 Entonces
			//*********Comparaciones********//
			// >, <, =, >=, <=, <>, -> mayor que, menor que, igual que...
			Escribir "El n�mero elegido vs el comparado es mayor ? ", numeroElegido > numeroAComparar
			Escribir "El n�mero elegido vs el comparado es menor ? ",  numeroElegido < numeroAComparar
			Escribir "El n�mero elegido vs el comparado es igual ? ",  numeroElegido == numeroAComparar
			Escribir "El n�mero elegido vs el comparado es mayor o igual que ? ",  numeroElegido >= numeroAComparar
			Escribir "El n�mero elegido vs el comparado es menor o igual que  ? ",  numeroElegido <= numeroAComparar
			Escribir "El n�mero elegido vs el comparado es distinto ? ",  numeroElegido <> numeroAComparar
		SiNo
		Escribir "NO elegiste un n�mero del rango indicado"
		Fin Si 
	SiNo
	Escribir "NO elegiste un n�mero del rango indicado"
	Fin Si
	FinAlgoritmo

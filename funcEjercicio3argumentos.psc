Funcion r <- suma ( n1,n2 )
	r<- n1+n2
Fin Funcion

//Ashly
Funcion imprimiendoNombre ( nombre)
	nombre = nombre
	Escribir nombre
FinFuncion

//Luna
Funcion mostrarMensaje
	Escribir "Este es un mensaje que fue invocado por funci�n"
FinFuncion

// RETO: CREAR UNA FUNCI�N QUE RECIBA 3 ARGUMENTOS: NUMERO, STRING Y TRUE O FALSE

Funcion retoTresArgumentos(edad, nombre, isTeacher)
	Escribir "Hola, mi nombre es: ", nombre, " tengo ", edad, ", �Soy maestro? ", isTeacher
FinFuncion

// Completar las funciones con resta, multiplicaci�n y divisi�n

Algoritmo funcEjercicio3Argumentos
	Escribir "El resultado de la suma de mi funci�n es: ", suma(9,8)
	imprimiendoNombre("Kevin")
	mostrarMensaje
	retoTresArgumentos(30, "Kevin", Verdadero)
	//Las dem�s funciones ac� ??
FinAlgoritmo
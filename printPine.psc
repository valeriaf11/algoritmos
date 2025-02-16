Algoritmo printPine
	Definir n, i, j Como Entero
    // Ask the user for the number of levels of the pine tree
    Escribir "Enter the number of levels of the pine: "
    Leer n
	
    Para i <- 1 Hasta (n - 1) Hacer
        Para j <- 1 Hasta (n - i) Hacer
            Escribir Sin Saltar " "
        FinPara
		// Print the asterisks forming the triangle
        Para j <- 1 Hasta (2 * i - 1) Hacer
            Escribir Sin Saltar "*"
        FinPara
        Escribir ""
    FinPara
	
    // Print spaces before the trunk
    Para j <- 1 Hasta (n - (n - 1)) Hacer
        Escribir Sin Saltar ""
    FinPara
    Para j <- 1 Hasta (2 * n - 1) Hacer
        Escribir Sin Saltar "*"
    FinPara
    Escribir ""
FinAlgoritmo

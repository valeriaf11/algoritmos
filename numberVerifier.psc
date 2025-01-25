Algoritmo numberVerifier
	// This program determines if a number is positive, negative, or zero.
	// It also checks if the number is even or odd.
    // Ask the user to enter a number.
    Escribir "Enter a number: "
    Leer number
    
    // Determine if the number is positive, negative, or zero.
    Si number > 0 Entonces
		Escribir "The number is positive."
    Sino 
		Si number < 0 Entonces
			Escribir "The number is negative."
		Sino
			Escribir "The number is zero."
		FinSi
    FinSi
    
    // Check if the number is even or odd.
    Si number <> 0 Entonces // Only check if the number is not zero
		Si number mod 2 = 0 Entonces
			Escribir "The number is even."
		Sino
			Escribir "The number is odd."
		FinSi
    FinSi

FinAlgoritmo

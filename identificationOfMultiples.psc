Algoritmo identificationOfMultiples
	//Determines if a number is a multiple of 3, 5 or both
	//Ask the user to enter an integer
	Escribir "Enter an integer"
	Leer integer 
	//Verify is the number is a multiple of 3 and 5 at the same time
	si integer%3=0 Y integer%5=0 Entonces
		// If the condition is true, display a message indicating it's a multiple of both
		Escribir integer " is multiple of 3 and 5 at the same time"
	SiNo
		// If the number is not a multiple of both 3 and 5, check if it's a multiple of 3 only
		si integer%3=0 Entonces
		    // If the condition is true, display a message indicating it's a multiple of 3
			Escribir integer " is multiple of 3"
		SiNo
			// If the number is not a multiple of 3, check if it's a multiple of 5 only
			si integer%5=0
			    // If the condition is true, display a message indicating it's a multiple of 5
				Escribir integer " is multiple of 5"
			SiNo
				//If it isn`t a multiple of any, send a message saying it doesn`t meet any conditions
				Escribir " Does not meet any conditions"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo

Algoritmo  bonusCalculator
	//Calculates the total salary after applying the corresponding bonus
	// Ask the user to enter their base salary
	Escribir "Enter your base salary"
	Leer baseSalary
	// Check if the base salary is less than 5000
	Si baseSalary < 5000 Entonces
		// Calculate the bonus (15%) if the salary is less than 5000
		bonus <- baseSalary * 0.15  // 15% bonus
		// Inform the user about the 15% bonus applied
        Escribir "The applied bonus is 15%: ", bonus
	SiNo 
		// Calculate the bonus (10%) if the salary is 5000 or more
		bonus <- baseSalary * 0.10 
        // Inform the user about the 10% bonus applied
		Escribir "The applied bonus is 10%: ", bonus
	FinSi
	// Calculate the total salary by adding the bonus to the base salary
    totalSalary <- baseSalary + bonus
	// Show total salary 
    Escribir "Your total salary after applying the bonus is: ", totalSalary
	
	
FinAlgoritmo

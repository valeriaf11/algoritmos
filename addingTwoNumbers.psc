//the Function command is used to create a block of code that performs a specific task
//and that it can be reused in various parts of the program.
//For example, if you need to add two numbers multiple times in your code, instead of writing the sum over and over again,
//you can create a function called Add and use it whenever you need it.
Funcion SumNumbers(a, b)
    Escribir "The sum is: ", a + b
FinFuncion

Algoritmo addingTwoNumbers
    Definir num1, num2 Como Real
    Escribir "enter two numbers:"
    Leer num1, num2
    SumNumbers(num1, num2)  // Parameter function call
FinAlgoritmo


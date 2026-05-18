//Ejercicio2
#include <stdio.h>

int main()
{
    int num1, num2, suma, resta, mult, mod;
   
    printf("Ingrese el primer numero entero: ");
    scanf("%d", &num1);
   
    printf("Ingrese el segundo numero entero: ");
    scanf("%d", &num2);
   
    suma = num1 + num2;
    resta = num1 - num2;
    mult = num1 * num2;
    mod = num1 % num2;
   
    printf("La suma entre %d y %d es: %d\n", num1, num2, suma);
    printf("La resta entre %d y %d es: %d\n", num1, num2, resta);
    printf("La multiplicacion entre %d y %d es: %d\n", num1, num2, mult);
    printf("El modulo entre %d y %d es: %d\n", num1, num2, mod);

    return 0;
}
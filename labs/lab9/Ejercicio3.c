//Ejercicio 3
#include <stdio.h>

int main()
{
    int base, altura, area, perimetro;
   
    printf("Ingrese la base: ");
    scanf("%d", &base);
   
    printf("Ingrese la altura: ");
    scanf("%d", &altura);
   
    area = base * altura;
    perimetro = (2*base) + (2*altura);
   
    printf("El area del rectangulo es: %d\n", area);
    printf("El perimetro del rectangulo es %d\n", perimetro);
   

    return 0;
}
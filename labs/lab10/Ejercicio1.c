#include <stdio.h>

int main()
{
    int num;
   
    printf("Ingrese el valor de temperatura: ");
    scanf("%d", &num);
   
    if (num<20) {
        printf("Estado: Subenfriamiento.\n");
    } else if (num>=20 && num<=45) {
        printf("Estado: Operacion Nominal.\n");
    } if (num>45) {
        printf("Estado: Alarma de sobrecalentamiento.\n");
    }
   

    return 0;
}
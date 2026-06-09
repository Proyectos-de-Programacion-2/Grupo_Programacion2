#include <stdio.h>

int main()
{
    int N;
    int contador = 0;
   
    printf("Ingresar valor limite N: ");
    scanf("%d", &N);
   
    for (int i = 0; i <= N; i++) {
        if (i%2 == 0) {
            printf("%d\n", i);
            contador++;
        }
    }
   
    printf("El total de numeros pares es: %d", contador);
    return 0;
}
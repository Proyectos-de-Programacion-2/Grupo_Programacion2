#include <stdio.h>

void duplicarValor(int *numero) {
    *numero = *numero * 2;
}

int main()
{
    int voltaje = 12;
    printf("Voltaje entrante: \n");
    printf("%d\n", voltaje);
   
    duplicarValor(&voltaje);
   
    printf("Voltaje saliente: \n");
    printf("%d", voltaje);

return 0;
}
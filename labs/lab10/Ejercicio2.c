#include <stdio.h>

int main()
{
    int opcion;
   
    do {
        printf("Ingrese una opcion (1-4): ");
        scanf("%d", &opcion);
       
        switch (opcion) {
            case 1:
                printf("Activar motor. \n");
                break;
            case 2:
                printf("Detener motor. \n");
                break;
            case 3:
                printf("Leer estado. \n");
                break;
            case 4:
                printf("Salir. \n");
                break;
        }
       
        if (opcion>4) {
            printf("Opcion no valida. \n");
        }
    } while (opcion != 4);

    return 0;
}
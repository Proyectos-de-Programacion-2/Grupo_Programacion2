# Ejercicio 1 - Ley de Ohm y Alerta de Potencia
V=float(input("Ingrese valor de Voltaje (V) "))
I=float(input("Ingrese el valor de Corriente (A) "))
R=V/I
P=V*I
print("El valor de la resistencia es:", (R), "Ohms") 
print("El valor de la potencia disipada es:", (P), "Watts")
if P>1000:
    print("¡PELIGRO! Alta disipacion de potencia disipada detectada.")
else:
    print("Operacion en rangos seguros.")

# Proyecto 1: Sistema de Análisis Robótico

## Descripción
Este directorio contiene la estructura principal para el sistema de análisis robótico. El proyecto está modularizado en distintos paquetes para separar la logica en base, modelos, analisis y visualizacion.

## Estructura del Proyecto
La carpeta está organizada de la siguiente manera:

```text
Proyecto1/
├── analisis/
│   └── __init__.py
│   └── analisis.py        # Funcion para analizar los datos de la simulacion utilizando Numpy
├── base/
│   └── __init__.py 
│   └── robot_base.py      # Logica comun, encapsulamiento y cinemartica de los robots     
├── modelos/
│   └── __init__.py
│   └── modelos_robot.py   # Clases de tipos de robots especificos que heredan de RobotBase, demostrando polimorfismo 
├── visualizacion/
│    └── __init__.py
│    └── visualizacion.py  # Funcion para graficar los resultados utilizando Matplotlib
├── main.py                # Script principal de ejecución
```

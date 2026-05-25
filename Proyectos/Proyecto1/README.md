# Proyecto 1: Sistema de Análisis Robótico

## Descripción
Este directorio contiene la estructura principal para el sistema de análisis robótico. El proyecto está modularizado en distintos paquetes para separar la logica en base, modelos, analisis y visualizacion.

## Estructura del Proyecto
La carpeta está organizada de la siguiente manera:

```text
Proyecto1/
└── analisis.py        # Funcion para analizar los datos de la simulacion utilizando Numpy
└── main.py            # Script principal de ejecución
└── modelos_robot.py   # Clases de tipos de robots especificos que heredan de RobotBase, demostrando polimorfismo
└── robot_base.py      # Logica comun, encapsulamiento y cinemartica de los robots
└── visualizacion.py   # Funcion para graficar los resultados utilizando Matplotlib
```

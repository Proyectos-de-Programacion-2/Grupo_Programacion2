import numpy as np
{}
def comparar_rendimiento(datos: list) ->dict

matriz = np.array(datos)
nombres_unicos = np.unique(matriz[:, 1])
diccionario_vacio = {}

for nombre in nombres_unicos:

    mascara = matriz[:, 1] == nombre 
    datos_robot = matriz[mascara]

    bateria = datos_robot[:, 4].astype(float)
    basura = datos_robot[:, 5].astype(float)

    bateria_f = bateria[-1]
    consumo_bateria = 100.0 - bateria_f

    basura_total = basura[-1]

    if consumo_bateria == 0.0:
        eficacia =0.0
    else: 
        eficiencia = basura_total / consumo_bateria
    
    
    resultados[nombre] ={
        "consumo_bateria" : float(consumo_bateria), 
        "basura_total" : float(basura_total),
        "eficiencia" : float(eficiencia)
    
    }
return resultados
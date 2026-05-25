import matplotlib.pyplot as plt
import numpy as np

def graficar_recoleccion_vs_bateria(resultados: dict):
   
    nombres_robots = list(resultados.keys())
    basura_total = [resultados[robot]['basura_total'] for robot in nombres_robots]
    consumo_bateria = [resultados[robot]['consumo_bateria'] for robot in nombres_robots]
    x = np.arange(len(nombres_robots))  
    ancho = 0.35  

    fig, ax = plt.subplots(figsize=(8, 6))
   
    ax.bar(x - ancho/2, basura_total, ancho, label='Basura Recolectada (kg)', color='green')
    ax.bar(x + ancho/2, consumo_bateria, ancho, label='Batería Consumida (%)', color='red')
    ax.set_title('Rendimiento: Recolección vs Consumo Energético')
    ax.set_ylabel('Cantidad')
    ax.set_xticks(x)
    ax.set_xticklabels(nombres_robots)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    fig.tight_layout()
    plt.show()
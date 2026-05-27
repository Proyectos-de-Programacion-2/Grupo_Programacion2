import pandas as pd
import os
from jugadores import jugador, portero, defensa, mediocampista, delantero

def main():
    
    pais = "Portugal"

    # Lista jugadores (datos de temporada 2025-2026, otros inventados por falta de info)
    jugadores_titulares = [
        portero("Diogo Costa", 26, 1.86, 1, atajadas=104, apariciones=49),
        defensa("João Cancelo", 31, 1.82, 20, balones_recuperados=203, despejes=178),
        defensa("Rúben Diaz", 29, 1.87, 3, balones_recuperados=189, despejes=140),
        defensa("Gonçalo Inácio", 24, 1.86, 14, balones_recuperados=147, despejes=98),
        defensa("Nuno Mendez", 23, 1.80, 25, balones_recuperados=195, despejes=176),
        mediocampista("João Neves", 21, 1.74, 15, asistencias=8, pases_efectivos=950),
        mediocampista("Vitinha", 26, 1.72, 23, asistencias=7, pases_efectivos=2572),
        mediocampista("Bruno Fernandes", 31, 1.79, 8, asistencias=21, pases_efectivos=1639),
        mediocampista("Bernardo Silva", 31, 1.73, 10, asistencias=4, pases_efectivos=1989),
        delantero("Rafael Leão", 26, 1.88, 17, goles=9, tiros_al_arco=45),
        delantero("Cristiano Ronaldo", 41, 1.87, 7, goles=28, tiros_al_arco=161)
    ]

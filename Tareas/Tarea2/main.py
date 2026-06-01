import pandas as pd
import os
from jugadores import jugador, portero, defensa, mediocampista, delantero

def main():
    print("\n--- SIMULADOR DE CAMPEÓN DEL MUNDO ---")

    pais = "Portugal"

    jugadores_titulares = [
        portero("Diogo Costa", 26, 1.86, 1, atajadas=104, apariciones=49),
        defensa("João Cancelo", 31, 1.82, 20, balones_recuperados=203, despejes=178),
        defensa("Rúben Dias", 29, 1.87, 3, balones_recuperados=189, despejes=140),
        defensa("Gonçalo Inácio", 24, 1.86, 14, balones_recuperados=147, despejes=98),
        defensa("Nuno Mendes", 23, 1.80, 25, balones_recuperados=195, despejes=176),
        mediocampista("João Neves", 21, 1.74, 15, asistencias=8, pases_efectivos=950),
        mediocampista("Vitinha", 26, 1.72, 23, asistencias=7, pases_efectivos=2572),
        mediocampista("Bruno Fernandes", 31, 1.79, 8, asistencias=21, pases_efectivos=1639),
        mediocampista("Bernardo Silva", 31, 1.73, 10, asistencias=4, pases_efectivos=1989),
        delantero("Rafael Leão", 26, 1.88, 17, goles=9, tiros_al_arco=45),
        delantero("Cristiano Ronaldo", 41, 1.87, 7, goles=28, tiros_al_arco=161),
    ]

    # Acciones en la cancha 
    print("\n--- ACCIONES EN LA CANCHA ---")
    for j in jugadores_titulares:
        print(j.correr())
    print(jugadores_titulares[0].atajar())
    print(jugadores_titulares[1].marcar())
    print(jugadores_titulares[5].dar_pase())
    print(jugadores_titulares[9].patear_al_arco())

    # Roles del equipo (Polimorfismo)
    print("\n--- ROLES DEL EQUIPO ---")
    for j in jugadores_titulares:
        # Se llama directamente al método mostrar_rol() de cada objeto
        print(f"{j.nombre} - {j.mostrar_rol()}") 

    # Creación de lista de diccionarios para Pandas
    datos_equipo = []
    for j in jugadores_titulares:
        datos_equipo.append({
            "Pais": pais,
            "Dorsal": j.dorsal,
            "Nombre": j.nombre,
            "Edad": j.edad,
            "Altura_m": j.altura,
            "Posicion": j.mostrar_rol()
        })

    # Creación del DataFrame
    df = pd.DataFrame(datos_equipo)

    print("\n--- ANÁLISIS DE PANDAS ---")
    print("\n1. Tabla completa del equipo:")
    print(df.to_string(index=False))
    print(f"\n2. Edad promedio del equipo: {df['Edad'].mean():.1f} años")
    print(f"3. Altura máxima del equipo: {df['Altura_m'].max()} m")
    print("\n4. Cantidad de jugadores por posición:")
    print(df['Posicion'].value_counts().to_string())
    print("\n5. Promedio de edad por posición:")
    print(df.groupby('Posicion')['Edad'].mean().to_string())

    # Exportación archivo CSV
    if not os.path.exists('output'):
        os.makedirs('output')
        
    ruta_archivo = 'output/titulares_portugal.csv'
    df.to_csv(ruta_archivo, index=False)
    print(f"\nArchivo exportado exitosamente a: {ruta_archivo}")

if __name__ == "__main__":
    main()

import pandas as pd
album = {
    "Cancion": ["Creep", "Persiana Americana", "Saturno", "Blue Monday"],
    "Artista": ["Radiohead", "Gustavo Cerati", "Pablo Alboran", "New Order"],
    "Duracion_segundos": [236, 270, 225, 449]
}
album = pd.DataFrame(album)
print(album)

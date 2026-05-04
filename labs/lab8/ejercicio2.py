import pandas as pd
datos = {
    " Componente ": [" Arduino ", " Resistencia 1k", " Capacitor ", " MotorDC"] ,
    " Stock ": [5 , 500 , 120 , 3]
}
df = pd.DataFrame(datos)
df_maximo = df[df[" Stock "] <10]
print(df_maximo)


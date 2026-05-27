# Clase Padre
class jugador:

    def __init__(self, nombre, edad, altura, dorsal):

        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dorsal = dorsal

    def correr(self):
        print(f"{self.nombre} esta corriendo.")

    def mostrar_rol(self):
        print("Soy un jugador de la seleccion de Portuguesa.")

    def celebrar(self):
        print(f"{self.nombre} celebra un gol.")
    
    def reclamo(self):
        print(f"{self.nombre} se acerca al arbitro y le reclama el penal cobrado.")

# Clase hija 1    
class portero(jugador):

    def __init__(self, nombre, edad, altura, dorsal, atajadas, apariciones):
        super().__init__(nombre, edad, altura, dorsal)
        self.atajadas = atajadas
        self.apariciones = apariciones

    def atajar(self):
        print(f"{self.nombre} ataja el tiro del rival.")

    def saque_de_arco(self):
        print(f"{self.nombre} realiza un saque de arco.")

    def mostrar_rol(self):
        return "Portero"

# Clase hija 2
class defensa(jugador):

    def __init__(self, nombre, edad, altura, dorsal, balones_recuperados, despejes):
        super().__init__(nombre, edad, altura, dorsal)
        self.balones_recuperados = balones_recuperados
        self.despejes = despejes

    def marcar(self):
        print(f"{self.nombre} está marcando al delantero rival.")

    def barrida(self):
        print(f"{self.nombre} realiza una barrida al rival.")

    def mostrar_rol(self):
        return "Defensa"

# Clase hija 3
class mediocampista(jugador):

    def __init__(self, nombre, edad, altura, dorsal, asistencias, pases_efectivos):
        super().__init__(nombre, edad, altura, dorsal)
        self.asistencias = asistencias
        self.pases_efectivos = pases_efectivos

    def dar_pase(self):
        print(f"{self.nombre} da un pase filtrado perfecto.")

    def posesion(self):
        print(f"{self.nombre} asegura la posesion del balon.")

    def mostrar_rol(self):
        return "Mediocampista"

#Clase hija 4
class delantero(jugador):

    def __init__(self, nombre, edad, altura, dorsal, goles, tiros_al_arco):
        super().__init__(nombre, edad, altura, dorsal)
        self.goles = goles
        self.tiros_al_arco = tiros_al_arco

    def patear_al_arco(self):
        print(f"{self.nombre} patea el balon hacia el arco rival.")

    def cabecear(self):
        print(f"{self.nombre} salta al balon elevado y cabecea.")

    def mostrar_rol(self):
        return "Delantero" 

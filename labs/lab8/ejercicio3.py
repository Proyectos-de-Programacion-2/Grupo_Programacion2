class Bateria:

    def __init__(self, marca):
      
        self.marca = marca
        self.__carga = 100

    def usar_bateria(self, gasto):
        new = self.__carga - gasto
        if new<=0:
            self.__carga = 0
            print("¡Bateria Agotada!")
        else:
            self.__carga = new
    

    def ver_carga(self):
       return(print(self.__carga))
    
mi_bateria = Bateria("Duracell")

mi_bateria.ver_carga()
mi_bateria.usar_bateria(40)
mi_bateria.ver_carga()
mi_bateria.usar_bateria(80)

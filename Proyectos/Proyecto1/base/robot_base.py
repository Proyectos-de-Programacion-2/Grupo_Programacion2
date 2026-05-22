import numpy as np

class RobotBase:
    def __init__(self, nombre, capacidad_carga, x_inicial=0.0,y_inicial=0.0, yaw_inicial=0.0):

        self.__nombre = nombre
        self.__capacidad_carga = capacidad_carga
        self.__bateria = 100.0 #%
        self.__pos_x = x_inicial
        self.__pos_y = y_inicial
        self.__yaw = yaw_inicial #rad
        self.__basura_recolectada = 0.0
        self.__step_dt = 0.1

        self.target_x = 5.0
        self.target_y = 5.0

    #Getters correspondientes
    def get_nombre(self):
        return self.__nombre
        
    def get_bateria(self):
        return self.__bateria
        
    def get_pos_x(self):
        return self.__pos_x
        
    def get_pos_y(self):
        return self.__pos_y
        
    def get_yaw(self):
        return self.__yaw
        
    def get_basura_recolectada(self):
        return self.__basura_recolectada
        
    # Metodos internos protegidos
    def _actualizar_pose(self, x, y, yaw):
        self.__pos_x = x
        self.__pos_y = y
        self.__yaw = yaw
        
    def _reducir_bateria(self, cantidad):
        new = self.__bateria - cantidad
        if new<=0:
            self.__bateria = 0
        else:
            self.__bateria = new

    def _recolectar_basura(self, cantidad):
        espacio_disponible = self.__capacidad_carga - self.__basura_recolectada
        
        if cantidad <= espacio_disponible:
            self.__basura_recolectada += cantidad
        else:
            self.__basura_recolectada += espacio_disponible

    # Metodos estaticos
    @staticmethod
    def calc_dist_to_goal(pos_x, pos_y, target_x, target_y):
        d = np.sqrt((target_x - pos_x)**2 + (target_y - pos_y)**2)
        return d
        
    @staticmethod
    def calc_yaw_error(pos_x, pos_y, yaw, target_x, target_y):
        ang_meta = np.atan2(target_y - pos_y, target_x - pos_x)

        err = ang_meta - yaw
        err_norm = (err + np.pi) % (2*np.pi) - np.pi
        return err_norm
        
    def step(self, v, w):
        if self.__bateria <= 0:
            return 0.0, True
            
        yaw_nuevo = self.__yaw + w*self.__step_dt
        yaw_nuevo_norm = (yaw_nuevo + np.pi) % (2*np.pi) - np.pi

        x_nuevo = self.__pos_x + v*np.cos(yaw_nuevo_norm)*self.__step_dt
        y_nuevo = self.__pos_y + v*np.sin(yaw_nuevo_norm)*self.__step_dt

        self._actualizar_pose(x_nuevo, y_nuevo, yaw_nuevo_norm)

        distancia = self.calc_dist_to_goal(self.__pos_x, self.__pos_y, self.target_x, self.target_y)
        error_angular = self.calc_yaw_error(self.__pos_x, self.__pos_y, self.__yaw, self.target_x, self.target_y)

        reward = -distancia - np.abs(error_angular)

        llegamos = False
        if distancia < 0.5:
            llegamos = True
            reward = reward + 100.0
            
        return (reward, llegamos)
        
    def mover(self):
        raise NotImplementedError("Las clases hijas deben implementar el método mover().")

    def limpiar(self):
        raise NotImplementedError("Las clases hijas deben implementar el método limpiar().")

        



        

        





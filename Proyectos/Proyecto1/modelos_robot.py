# modelos_robot.py

import random
from robot_base import RobotBase

# 1. RobotTresRuedas
class RobotTresRuedas(RobotBase):
    """
    Robot de limpieza con tres ruedas.
    Hereda de RobotBase y sobrescribe mover() y limpiar().
    """

    def __init__(self, nombre, radio_rueda):
        # Llama al constructor padre con capacidad de carga fija de 20 kg
        super().__init__(nombre, capacidad_carga=20.0)
        self.radio_rueda = radio_rueda      # Atributo propio del triciclo
        self.ruedas_calibradas = False      # Estado inicial: sin calibrar

    def calibrar_giro(self):
        """Calibra el sistema de giro e informa el radio de rueda usado."""
        print(f"[{self.get_nombre()}] Calibrando triciclo con ruedas de {self.radio_rueda} cm...")
        self.ruedas_calibradas = True

    def mover(self):
        """Movimiento equilibrado: velocidad moderada, giro suave."""
        return self.step(v=0.8, w=0.2)

    def limpiar(self):
        """Consume 2 % de batería y recoge entre 0.5 y 1.5 kg de basura."""
        self._reducir_bateria(2.0)
        basura = random.uniform(0.5, 1.5)
        self._recolectar_basura(basura)


# 2. RobotOruga
class RobotOruga(RobotBase):
    """
    Robot de limpieza tipo oruga (tanque).
    Alta capacidad de carga; movimiento lento pero con giro pronunciado.
    """

    def __init__(self, nombre, tension_oruga):
        # Llama al constructor padre con capacidad de carga de 50 kg
        super().__init__(nombre, capacidad_carga=50.0)
        self.tension_oruga = tension_oruga  # Tensión de la oruga en %

    def ajustar_tension(self):
        """Muestra la tensión configurada en las orugas."""
        print(f"[{self.get_nombre()}] Ajustando tension de las orugas al {self.tension_oruga} %.")

    def mover(self):
        """Movimiento lento con giro fuerte."""
        return self.step(v=0.3, w=0.8)

    def limpiar(self):
        """Consume 4.5 % de batería y recoge entre 2.0 y 4.0 kg de basura."""
        self._reducir_bateria(4.5)
        basura = random.uniform(2.0, 4.0)
        self._recolectar_basura(basura)


# 3. RobotDron
class RobotDron(RobotBase):
    """
    Robot de limpieza aéreo (dron).
    Poca capacidad de carga pero muy veloz; solo opera en vuelo.
    """

    def __init__(self, nombre, altura_maxima):
        # Llama al constructor padre con capacidad de carga reducida de 5 kg
        super().__init__(nombre, capacidad_carga=5.0)
        self.altura_maxima = altura_maxima  # Altura máxima de vuelo en metros
        self.en_vuelo = False               # Estado inicial: en tierra

    def despegar(self):
        """Inicia el vuelo e informa la altura máxima configurada."""
        print(f"[{self.get_nombre()}] Despegando hasta {self.altura_maxima}.0 metros de altura.")
        self.en_vuelo = True

    def mover(self):
        """Solo se mueve si está en vuelo; velocidad muy alta."""
        if self.en_vuelo:
            return self.step(v=2.5, w=1.0)
        # Si no está en vuelo, no realiza ningún movimiento
        return 0.0, False

    def limpiar(self):
        """Solo limpia si está en vuelo; recoge material ligero (0.1–0.4 kg)."""
        if self.en_vuelo:
            self._reducir_bateria(3.0)
            basura = random.uniform(0.1, 0.4)
            self._recolectar_basura(basura)

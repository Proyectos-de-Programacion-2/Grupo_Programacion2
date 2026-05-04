import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)

x = np.sin(t)

plt.plot(t, x, color='blue')
plt.title("Lectura de Sensor (Señal Senoidal)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

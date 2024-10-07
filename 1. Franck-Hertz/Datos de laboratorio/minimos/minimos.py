import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d

# Cargar los datos desde el archivo CSV
file_path = 'datos.csv'
data = pd.read_csv(file_path, sep=';')

# Convertir los datos a arrays numpy
voltaje = data['Voltaje U1'].values
corriente = data['Corriente IA'].values

# Suavizar la curva usando un filtro gaussiano
smoothed_corriente = gaussian_filter1d(corriente, sigma=3)

# Encontrar el mínimo de la curva suavizada
min_envolvente_index = np.argmin(smoothed_corriente)

# Encontrar los mínimos locales en la curva suavizada
minima_suavizada_indices, _ = find_peaks(-smoothed_corriente)  # Invertir la corriente suavizada para encontrar mínimos

# Crear un DataFrame con los resultados de los mínimos locales
minima_suavizada_voltajes = voltaje[minima_suavizada_indices]
minima_suavizada_corrientes = smoothed_corriente[minima_suavizada_indices]

minima_suavizada_df = pd.DataFrame({
    'Voltaje U1': minima_suavizada_voltajes,
    'Corriente IA Suavizada': minima_suavizada_corrientes
})

# Mostrar los resultados de los mínimos locales
print(minima_suavizada_df)

# Plotear la curva original, la curva suavizada, y los mínimos locales
plt.figure(figsize=(10, 6))
plt.plot(voltaje, corriente, label="Corriente IA", color='blue')
plt.plot(voltaje, smoothed_corriente, label="Curva Suavizada", color='orange', linestyle='--')
plt.plot(voltaje[minima_suavizada_indices], smoothed_corriente[minima_suavizada_indices], 'ro', label='Mínimos Locales Suavizados')
plt.title('Gráfica de Voltaje vs Corriente IA con Mínimos Locales de la Curva Suavizada')
plt.xlabel('Voltaje U1')
plt.ylabel('Corriente IA Suavizada')
plt.legend()
plt.grid(True)
plt.show()


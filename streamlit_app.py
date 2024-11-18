import streamlit as st
# Importar las librerías necesarias
import rpy2.robjects as ro
import pandas as pd
# Crear un DataFrame en Python
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11]
}
df_python = pd.DataFrame(data)

# Crear manualmente un DataFrame de R a partir del DataFrame de Pandas
r_x = ro.FloatVector(df_python['x'])  # Convertir columna 'x' a un vector de R
r_y = ro.FloatVector(df_python['y'])  # Convertir columna 'y' a un vector de R

# Crear el data frame de R
df_r = ro.DataFrame({'x': r_x, 'y': r_y})

# Cargar el paquete necesario en R
ro.r('library(stats)')

# Asignar el DataFrame de R a una variable en R
ro.r.assign('df', df_r)

# Realizar una regresión lineal en R
ro.r('model <- lm(y ~ x, data = df)')

# Obtener el resumen del modelo
summary = ro.r('summary(model)')

# Imprimir el resumen
print(summary)
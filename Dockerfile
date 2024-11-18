# Usa una imagen base de Python
FROM python:3.11-slim

# Instalar R y las dependencias necesarias
RUN apt-get update && apt-get install -y \
    r-base \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Configura el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt en el contenedor
COPY requirements.txt /app/

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar rpy2
RUN pip install rpy2

# Copiar el código fuente del proyecto en el contenedor
COPY . /app/

# Expone el puerto donde correrá Streamlit
EXPOSE 8501

# Comando para ejecutar Streamlit
CMD ["streamlit", "run", "app.py"]

# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto en el contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install Flask openai==0.28

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Define el comando para iniciar la aplicación
CMD ["python", "cuentacuentos.py"]

# Obtener imágen base.
FROM python:3.10-slim-bullseye

# Configurar variables de entorno.
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Configuración de la librería de trabajo.
WORKDIR /final

# Instalar dependencias.
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar proyecto.
COPY . .
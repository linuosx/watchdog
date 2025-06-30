# Utiliza una imagen oficial de Python
FROM python:3.13-slim

WORKDIR /app

COPY url_test.py ./
# COPY pyproject.toml ./
# COPY pdm.lock ./

# Instala dependencias (usa pip si no tienes pdm configurado en la imagen)
RUN pip install requests python-decouple

# Copia el entrypoint que ejecuta el script cada minuto
COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]

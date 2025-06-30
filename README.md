# Watchdog URL Test

Este proyecto es un script en Python diseñado para monitorear la disponibilidad de una URL y notificar errores a un canal de Slack mediante un webhook. Es ideal para entornos de desarrollo o pruebas donde se requiere supervisión básica de endpoints.

## Características
- Realiza solicitudes HTTP GET a una URL configurable.
- Notifica automáticamente a Slack si la URL no responde correctamente o si ocurre un timeout.
- Configuración flexible mediante variables de entorno.
- Permite personalizar el User-Agent y el Host de la solicitud.

## Requisitos
- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [python-decouple](https://pypi.org/project/python-decouple/)

## Instalación
1. Clona este repositorio:
   ```bash
   git clone <REPO_URL>
   cd watchdog
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   O si usas [PDM](https://pdm.fming.dev/):
   ```bash
   pdm install
   ```

## Configuración
Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
SLACK_WEBHOOK_URL=<tu_webhook_de_slack>
URL=<url_a_monitorear>
REQUEST_TIMEOUT=30
HOSTNAME=localhost
```

- `SLACK_WEBHOOK_URL`: URL del webhook de Slack para notificaciones.
- `URL`: Endpoint a monitorear.
- `REQUEST_TIMEOUT`: (Opcional) Tiempo de espera en segundos para la solicitud HTTP (por defecto 30).
- `HOSTNAME`: (Opcional) Host a usar en la cabecera de la solicitud (por defecto 'localhost').

## Uso
Ejecuta el script principal:

```bash
python src/url_test.py
```

El script realizará una solicitud a la URL configurada y notificará a Slack si hay errores o timeouts. Si la respuesta es exitosa, mostrará los primeros 100 caracteres del contenido recibido en el log.

## Docker
Incluye un `Dockerfile` y un `docker-compose.yml` para facilitar la ejecución en contenedores.

## Licencia
MIT

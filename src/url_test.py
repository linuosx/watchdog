import requests
import logging
from decouple import config

# Configura tu webhook de Slack aquí
SLACK_WEBHOOK_URL = config('SLACK_WEBHOOK_URL')

def notificar_slack(mensaje: str):
    payload = {"text": mensaje}
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error al enviar mensaje a Slack: {e}")

def do_request(url: str):
    try:
        response = requests.get(
            url, 
            timeout=config('REQUEST_TIMEOUT', cast=int, default=30),
            headers={
                'User-Agent': 'Watchdog/1.0',
                "Host": config('HOSTNAME', default='localhost')
            },
            verify=False  # No verifica el certificado SSL debido a que es una conexión local o de desarrollo
        )
        if response.status_code != 200:
            notificar_slack(f"Error en la solicitud a {url}: Código {response.status_code}")
        else:
            return response.text
    except requests.Timeout:
        notificar_slack(f"Timeout al intentar acceder a {url} después de 30 segundos.")
    except requests.RequestException as e:
        notificar_slack(f"Error general al acceder a {url}: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    url = config('URL')
    resultado = do_request(url)
    if resultado:
        logging.info(f"Contenido recibido de {url}: {resultado[:100]}...")  # Muestra los primeros 100 caracteres

import requests
import random
import time

# URL de acción del formulario de Google
URL_FORMULARIO = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSeVoEtg7SFOYF1cdamQzLaSVIQblxeVqb2zwSmlAnMfiiS8Wg/formResponse"

# Opciones extraídas del HTML para cada tipo de pregunta
opciones_basicas = ["Si", "No", "A veces"]
opciones_q4 = [
    "Me motivan a elegir una carrera o profesión específica.",
    "Me hacen considerar opciones que ellos prefieren.",
    "Me generan dudas o inseguridad sobre mis propias decisiones.",
    "Me generan presión para tomar determinadas decisiones.",
    "No influyen en mis decisiones."
]
opciones_q9 = [
    "Presión para obtener buenas calificaciones.",
    "Presión para elegir una determinada carrera o profesión.",
    "Presión por cumplir con sus expectativas.",
    "Presión por compararme con hermanos, compañeros u otras personas.",
    "No siento presión por parte de mis padres."
]

def enviar_encuesta_aleatoria():
    # Diccionario con los IDs de los 'entry' extraídos del formulario
    datos = {
        "entry.93386106": random.choice(opciones_basicas),
        "entry.1745144288": random.choice(opciones_basicas),
        "entry.969711172": random.choice(opciones_basicas),
        "entry.91491116": random.choice(opciones_q4),
        "entry.295198287": random.choice(opciones_basicas),
        "entry.1686116906": random.choice(opciones_basicas),
        "entry.1856092365": random.choice(opciones_basicas),
        "entry.294477485": random.choice(opciones_basicas),
        "entry.564005540": random.choice(opciones_q9),
        "entry.1274193837": random.choice(opciones_basicas)
    }

    try:
        # Enviamos la petición POST para registrar la respuesta
        respuesta = requests.post(URL_FORMULARIO, data=datos)
        if respuesta.status_code == 200:
            print("Encuesta inyectada correctamente.")
        else:
            print(f"Error al enviar. Código: {respuesta.status_code}")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == '__main__':
    # Configura los límites de cantidad de encuestas que quieres generar aleatoriamente
    LIMITE_MINIMO = 15
    LIMITE_MAXIMO = 50

    # Selección aleatoria de la cantidad de veces que se llenará el formulario
    cantidad_iteraciones = random.randint(LIMITE_MINIMO, LIMITE_MAXIMO)
    print(f"Se ha decidido inyectar datos en el formulario {cantidad_iteraciones} veces de forma aleatoria.")

    for i in range(cantidad_iteraciones):
        print(f"Enviando iteración {i + 1} de {cantidad_iteraciones}...")
        enviar_encuesta_aleatoria()
        
        # Pausa aleatoria entre 1 y 3 segundos para emular comportamiento humano
        time.sleep(random.uniform(1, 3))

    print("Proceso de inyección finalizado con éxito.")

import time
import requests
import random

SERVER_URL = "http://iot_server:8080"

while True:
    payload = {
        "temperature": random.randint(20, 30),
        "humidity": random.randint(40, 60)
    }
    try:
        requests.post(SERVER_URL, json=payload, timeout=2)
    except:
        pass

    time.sleep(5)  # Send data every 5 seconds

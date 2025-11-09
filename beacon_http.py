# -*- coding: utf-8 -*-
import time, requests

BEACON_INTERVAL = 30  # secondes entre chaque requête
ID = "TahaLab"
url = "http://127.0.0.1:8000/ping?id=" + ID

while True:
    try:
        r = requests.get(url, timeout=10)
        print(time.strftime("%H:%M:%S"), "->", r.status_code)
    except Exception as e:
        print(time.strftime("%H:%M:%S"), "ERR", e)
    time.sleep(BEACON_INTERVAL)

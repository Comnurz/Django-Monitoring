import os

import psutil
import requests
from time import sleep

BASE_URL = os.environ.get("MONITORING_URL", "http://localhost:8000/en")
DBSAVE_URL = BASE_URL.rstrip('/') + '/api/dbsave/'

with open('servertoken.txt', 'r') as f:
    token = f.read().strip()

headers = {"Authorization": "Token " + token}

while True:
    # expected output: total:xxxxxx used:xxxxxx free:xxxxxx
    # percent:xxxxxx sin:xxxxxx sout:xxxxxx
    ramdata = psutil.swap_memory()

    # expected output: percent:xxxxxx
    cpudata = psutil.cpu_percent(interval=1)

    # expected output: total: xxxxxx used:xxxxxx free:xxxxxx percent:xxxxxx
    diskdata = psutil.disk_usage('/')

    payload = {
        "ram": list(ramdata),
        "cpu": [cpudata],
        "disk": list(diskdata),
    }
    requests.post(DBSAVE_URL, json=payload, headers=headers, timeout=10)
    sleep(60)

import os
import sys
import subprocess
from getpass import getpass

import requests

BASE_URL = os.environ.get("MONITORING_URL", "http://localhost:8000/en")
REGISTER_URL = BASE_URL.rstrip('/') + '/api/register/'

user_name: str = input("Please Enter Username: ")
password: str = getpass("Please Enter Password: ")
server: str = input("Please Enter Server Name: ")

response = requests.post(REGISTER_URL, json={
    "username": user_name,
    "password": password,
    "server_name": server,
}, timeout=10)

if response.status_code == 200 and response.json().get("token"):
    token = response.json()["token"]
    print("Success.")
    fd = os.open("servertoken.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as tokenfile:
        tokenfile.write(token)
    subprocess.Popen([sys.executable, "server.py"])
else:
    print("Wrong given data!")

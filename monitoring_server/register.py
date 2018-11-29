import requests
import subprocess
from getpass import getpass

# get data from user for check
user_name: str = input("Please Enter Username: ")
password: str = getpass("Please Enter Password: ")
server: str = input("Please Enter Server Name: ")

# Check User and Server ID
server_id = requests.get("http://localhost:8000/en/user", params={
            "username": user_name, "password": password, "server_name": server
        })

server_id = str(server_id.content).replace("b", "")
server_id = server_id.replace("\'", "")

if server_id:
    print("Success.")
    serverid = open("serverid.txt", "w+")
    serverid.write(server_id)
    serverid.close()
    subprocess.call("nohup python3 server.py &", shell=True)
else:
    print("Wrong given data!")

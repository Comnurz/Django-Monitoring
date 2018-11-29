import psutil
import requests
from time import sleep

url = 'http://localhost:8000/en/dbsave/'

serverid = open('serverid.txt', 'r+')
server_id = serverid.read()

while True:
    # expected output: total:xxxxxx used:xxxxxx free:xxxxxx
    # percent:xxxxxx sin:xxxxxx sout:xxxxxx
    ramdata = psutil.swap_memory()

    # expected output: percent:xxxxxx
    cpudata = psutil.cpu_percent(interval=1)

    # expected output: total: xxxxxx used:xxxxxx free:xxxxxx percent:xxxxxx
    diskdata = psutil.disk_usage('/')

    # Data post
    requests.post(url, params={"ram": ramdata, "cpu": cpudata,
                  "disk": diskdata, "server": server_id})
    sleep(60)

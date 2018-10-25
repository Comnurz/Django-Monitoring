import psutil
import requests
from time import sleep
from getpass import getpass

url='http://localhost:8080/en/dbsave/'

serverid=open('serverid.txt','r+')
server_id=serverid.read()

while True:
    ramdata=psutil.swap_memory() # expected output: total:xxxxxx used:xxxxxx free:xxxxxx percent:xxxxxx sin:xxxxxx sout:xxxxxx

    cpudata=psutil.cpu_percent(interval=1) # expected output: percent:xxxxxx

    diskdata=psutil.disk_usage('/')# expected output: total: xxxxxx used:xxxxxx free:xxxxxx percent:xxxxxx

    requests.post(url,params={"ram":ramdata,"cpu":cpudata,"disk":diskdata,"server":server_id} )    # Data post
    sleep(60)

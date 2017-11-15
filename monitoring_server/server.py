import psutil
import requests
from time import sleep
from getpass import getpass

url='http://localhost:8000/dbsave/'

#get data from user for check 
user_name=input("Please Enter Username: ")
password=getpass("Please Enter Password: ")
server=input("Please Enter Server Name: ")

# Check User and Server ID
server_id=requests.get('http://localhost:8000/user',params={
"username":user_name,"password":password,"server_name":server
})

if server_id:
    print("Success!")
    while True:
        ramdata=psutil.swap_memory() # expected output: total:xxxxxx used:xxxxxx free:xxxxxx percent:xxxxxx sin:xxxxxx sout:xxxxxx

        cpudata=psutil.cpu_percent(interval=1) # expected output: percent:xxxxxx

        diskdata=psutil.disk_usage('/')# expected output: total: xxxxxx used:xxxxxx free:xxxxxx percent:xxxxxx

        requests.post(url,params={"ram":ramdata,"cpu":cpudata,"disk":diskdata,"server":server_id} )    # Data post
        sleep(60)
else:
    print("Wrong Given Data")

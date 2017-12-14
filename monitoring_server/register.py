import requests
import subprocess
from getpass import getpass

# get data from user for check
user_name=input("Please Enter Username: ")
password=getpass("Please Enter Password: ")
server=input("Please Enter Server Name: ")

# Check User and Server ID
server_id=requests.get('http://localhost:8000/user',params={
"username":user_name,"password":password,"server_name":server
})

server_id=str(server_id.content).replace('b',"")
server_id=server_id.replace('\'',"")

if server_id:
    print ("Success.")
    serverid=open('serverid.txt','r+')
    serverid.write(server_id)
    serverid.close()
    subprocess.call("./server.sh", shell=True)
else:
    print ("Wrong given data!")

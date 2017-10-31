# Django-Monitoring
Django monitoring web application

server.py run on your server which want to get data.

Run this commant in your server terminal:

```
pip install -r serverrequirements.txt
```

Run this commant in your local terminal:

```
pip install -r requirements.txt
```

You have to change this lines of code before use:

#### server.py 
 * line: 38  
```
run(host='HOST', port=PORT)
```
#### views.py
 * line: 18
```
resRam = requests.get('http://HOST:PORT/ramdata')
```
 * line: 21
```
resCpu = requests.get('http://HOST:PORT/cpudata')
```
 * line: 24 
```
resDisk = requests.get('http://HOST:PORT/diskdata')
```

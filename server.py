from bottle import run, template, get, post, request
import psutil

# server url (example: host:post/ramdata)
@get('/ramdata')
def ram():
    data=[]
    ramdata=psutil.swap_memory()
    # output = sswap(total=2097147904, used=296128512, free=1801019392, percent=14.1, sin=304193536, sout=677842944)
    out=["total","used","free","percent","sin","sout"]
    for i in range (len(ramdata)):
        data.append([out[i],ramdata[i]])

    return {'response': data}


@get('/cpudata')
def cpu():
    data=[]
    cpudata=psutil.cpu_percent(interval=1)
    # Used cpu percent / output = 4.0 etc.
    out=["percent"]
    data.append([out[0],cpudata])
    return {'response': data}

@get('/diskdata')
def disk():
    data=[]
    diskdata=psutil.disk_usage('/')
    # output = sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
    out=["total","used","free","percent"]
    for i in range (len(diskdata)):
        data.append([out[i],diskdata[i]])

    return {'response': data}

# make api call
run(host='localhost', port=8080)

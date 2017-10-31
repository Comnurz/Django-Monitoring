from bottle import run, template, get, post, request
import psutil

# server url (example: host:post/ramdata)
@get('/ramdata')
def ram():
    data=[]
    # output = sswap(total=2097147904, used=296128512, free=1801019392, percent=14.1, sin=304193536, sout=677842944)
    ramdata=psutil.swap_memory()
    out=["total","used","free","percent","sin","sout"]
    for i in range (len(ramdata)):
        data.append([out[i],ramdata[i]])

    return {'response': data}


@get('/cpudata')
def cpu():
    data=[]
    # Used cpu percent / output = 4.0 etc.
    cpudata=psutil.cpu_percent(interval=1)
    out=["percent"]
    data.append([out[0],cpudata])
    return {'response': data}

@get('/diskdata')
def disk():
    data=[]
    # output = sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
    diskdata=psutil.disk_usage('/')
    out=["total","used","free","percent"]
    for i in range (len(diskdata)):
        data.append([out[i],diskdata[i]])

    return {'response': data}

# make api call
run(host='HOST', port=PORT)

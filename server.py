import psutil
import requests

ram=[]
# expected output: total:xxxxxx used:xxxxxx free:xxxxxx percent:xxxxxx sin:xxxxxx sout:xxxxxx
ramdata=psutil.swap_memory()
# ram data types for editing
ramout=["total","used","free","percent","sin","sout"]
for i in range(len(ramdata)):
    # editing ram array list like "total:data used:data free:data percent:data sin:data sout:data"
    ram.append([ramout[i],ramdata[i]])
# post data to url
requests.post("/ramdata",params=ram)

cpu=[]
# expected output: percent:xxxxxx
cpudata=psutil.cpu_percent(interval=1)
# cpu data type for editing
cpuout=["percent"]
for i in range(len(cpudata)):
    # editing cpu array list like "percent:data"
    cpu.append([cpuout[i],cpudata[i]])
# post data to url
requests.post("/cpudata",params=cpu)

disk=[]
# expected output: total: xxxxxx used:xxxxxx free:xxxxxx percent:xxxxxx
diskdata=psutil.disk_usage('/')
# disk data types for editing
diskout=["total","used","free","percent"]
for i in range(len(diskdata)):
    # editing disk array list like "total: data used:data free:data percent:data"
    disk.append([diskout[i],diskdata[i]])
# post data to url
requests.post("/diskdata",params=disk)

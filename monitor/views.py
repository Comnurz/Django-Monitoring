from django.shortcuts import render
import requests
# Create your views here.
def index(request):  
  ramValues,diskValues,cpuValues=requestData() 
  return render(request, 'monitor/index.html', { 
    'ramValues': ramValues, 
    'diskValues':diskValues,
    'cpuValues':cpuValues 
 
    }) 
 
def requestData(): 
  cpuList= [] 
  ramList=[] 
  diskList=[['a',123]] 
  reqRam = requests.get('http://localhost:8080/ramdata') 
  ramList=listBuilder(reqRam) 
  reqCpu = requests.get('http://localhost:8080/cpudata')  
  cpuList=listBuilder(reqCpu) 
  reqDisk = requests.get('http://localhost:8080/diskdata') 
  diskList=listBuilder(reqDisk) 
 
  return ramList,diskList ,cpuList 
 
def listBuilder(l): 
  newList=[] 
  jsonData=l.json() 
  items=jsonData.values() 
  for item in items: 
    for key in item: 
      newList.append([key[0],key[1]]) 
  return newList
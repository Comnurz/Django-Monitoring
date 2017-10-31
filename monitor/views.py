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
  diskList=[]
  # get ram data
  resRam = requests.get('http://HOST:PORT/ramdata')
  ramList=listBuilder(resRam)
  # get cpu data
  resCpu = requests.get('http://HOST:PORT/cpudata')
  cpuList=listBuilder(resCpu)
  # get disk data
  resDisk = requests.get('http://HOST:PORT/diskdata')
  diskList=listBuilder(resDisk)

  return ramList,diskList ,cpuList

# building a list for Google Charts
def listBuilder(l):
  newList=[]
  jsonData=l.json()
  items=jsonData.values()
  for item in items:
    for key in item:
      newList.append([key[0],key[1]])
  return newList

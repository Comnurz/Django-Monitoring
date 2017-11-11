from django.shortcuts import render
import requests

from django.http import request, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from monitor.models import Ram,Cpu,Disk,Server
from django.contrib.auth.models import User

@api_view(['POST','OPTIONS'])
def dbSave(request):
    ram=request.GET.getlist('ram','')
    cpu=request.GET.getlist('cpu','')
    disk=request.GET.getlist('disk','')
    server=request.GET.get('server','')

    ramSave(ram,server)
    cpuSave(cpu,server)
    diskSave(disk,server)
    return Response(True)
def ramSave(detail,server):
    server=Server.objects.get(id=server)
    ram=Ram(total=detail[0],used=detail[1],free=detail[2],percent=float(detail[3]),sin=detail[4],sout=detail[5],server_id=server)
    ram.save()

def cpuSave(detail,server):
    server=Server.objects.get(id=server)
    cpu=Cpu(percent=float(detail[0]),server_id=server)
    cpu.save()

def diskSave(detail,server):
    server=Server.objects.get(id=server)
    disk=Disk(total=detail[0],used=detail[1],free=detail[2],percent=float(detail[3]),server_id=server)
    disk.save()


# Create your views here.
def index(request):
  ramValues,diskValues,cpuValues=requestData()
  return render(request, 'monitor/index.html', {
    'ramValues': ramValues,
    'diskValues':diskValues,
    'cpuValues':cpuValues

    })
def ramData(request):
    ramValues=request.body

    return render(request,'monitor/ramdata.html',{'ramValues':ramValues})


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

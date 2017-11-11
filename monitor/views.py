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
  ram=Ram.objects.all()
  disk=Disk.objects.all()
  cpu=Cpu.objects.all()
  ramValues=[]
  diskValues=[]
  cpuValues=[]
  ramUsed=[]
  for i in ram:

      ramValues.append([i.date.time,i.percent])
      ramUsed.append([i.date.time,i.used])
      print(i.used)
  for j in disk:
      diskValues.append([j.date.time,j.percent])
  for k in cpu:
      cpuValues.append([k.date.time,k.percent])

  return render(request, 'monitor/index.html', {
    'ramValues': ramValues,
    'ramUsed':ramUsed,
    'diskValues':diskValues,
    'cpuValues':cpuValues
    })

import requests

from django.http import request, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from monitor.forms import SignUpForm
from django.shortcuts import render, redirect

from monitor.models import Ram,Cpu,Disk,Server,Server_User
from django.contrib.auth.models import User

from .forms import ServerForm

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

def server(request):
    if request.method== 'POST':
        form=ServerForm(request.POST)
        if form.is_valid():
            form.save()
            server_name=form.cleaned_data.get('server_name')
            return redirect('index')
    else:
        form=ServerForm()
    return render(request,'registration/server.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('server')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

import requests
import json

from django.http import request, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from monitor.forms import SignUpForm, ServerForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from django.core import serializers

from monitor.models import Ram,Cpu,Disk,Server,Server_User
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256

@api_view(['POST','OPTIONS'])
def dbSave(request):
    # Get request data
    ram=request.GET.getlist('ram','')
    cpu=request.GET.getlist('cpu','')
    disk=request.GET.getlist('disk','')
    server=request.GET.get('server','')

    # Save given data
    ramSave(ram,server)
    cpuSave(cpu,server)
    diskSave(disk,server)

    return Response(True)

def ramSave(detail,server):
    server=Server.objects.get(id=server) #get Server objects which id=server
    ram=Ram(total=detail[0],used=detail[1],free=detail[2],percent=float(detail[3]),sin=detail[4],sout=detail[5],server_id=server)#save data to ram
    ram.save()

def cpuSave(detail,server):
    server=Server.objects.get(id=server)#get Server objects which id=server
    cpu=Cpu(percent=float(detail[0]),server_id=server)  #save data to cpu
    cpu.save()

def diskSave(detail,server):
    server=Server.objects.get(id=server)#get Server objects which id=server
    disk=Disk(total=detail[0],used=detail[1],free=detail[2],percent=float(detail[3]),server_id=server)#save data to disk
    disk.save()

# Create your views here.
def detail(request):
    current_user=request.user

    server_userobj=Server_User.objects.filter(user_id=current_user.id).exists() #check server user pairing
    if server_userobj:
        servers=[]
        server=Server_User.objects.filter(user_id=current_user.id).values_list('server_id',flat=True)
        for i in range(len(server)):
            servers.append(Server.objects.get(id=server[i]))
        return render(request, 'monitor/detail.html', {'servers': servers})
    else:
        return redirect('server')


def cpu_chart(request,pk):
    json_serializer=serializers.get_serializer("json")()

    cpus = json_serializer.serialize(Cpu.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1], ensure_ascii=False)
    cpuExists=Cpu.objects.all().filter(server_id=pk).exists()

    if cpuExists:
        return render(request, 'monitor/cpu_chart.html', {
        'cpuValues': cpus,
        })
    else:
        return redirect('howtosetup')

def disk_chart(request,pk):
    json_serializer=serializers.get_serializer("json")()

    disks = json_serializer.serialize(Disk.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1], ensure_ascii=False)
    diskExists=Disk.objects.all().filter(server_id=pk).exists()

    if diskExists:
        return render(request, 'monitor/disk_chart.html', {
        'diskValues': disks,
        })
    else:
        return redirect('howtosetup')

def ram_chart(request,pk):
    json_serializer=serializers.get_serializer("json")()

    rams = json_serializer.serialize(Ram.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1], ensure_ascii=False)
    ramExists=Ram.objects.all().filter(server_id=pk).exists()

    if ramExists:
        return render(request, 'monitor/ram_chart.html', {
        'ramValues': rams,
        })
    else:
        return redirect('howtosetup')

def chart(request,pk):
    json_serializer = serializers.get_serializer("json")()

    '''
    mysql command is : "select * from Ram where server_id=pk orderby id desc 28"
    or this command be like this:
    ramValues=Ram.objects.all() --> get all ram objects
    filteredRamValues=ramValues.filter(server_id=pk) --> ramValues filter by server_id
    orderedRamValues=filteredRamValues.order_by('-id')[:28] --> get ramValues last 28 item
    reversedRamValues=reversed(orderedRamValues) --> this command is reversed ramValues
    rams=json_serializer.serialize(reversedRamValues) --> get json from ramValues
    '''
    rams = json_serializer.serialize(Ram.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1], ensure_ascii=False)
    ramExists=Ram.objects.all().filter(server_id=pk).exists()

    cpus = json_serializer.serialize(Cpu.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1], ensure_ascii=False)
    cpuExists=Cpu.objects.all().filter(server_id=pk).exists()

    disks = json_serializer.serialize(Disk.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1], ensure_ascii=False)
    diskExists=Disk.objects.all().filter(server_id=pk).exists()

    # if expected data is exists, go to the how to setup.
    if ramExists and cpuExists and diskExists:
        return render(request, 'monitor/chart.html', {
        'ramValues': rams,
        'diskValues':disks,
        'cpuValues':cpus
        })
    else:
        return redirect('howtosetup')

def howtosetup(request):
    return render(request,'monitor/howtosetup.html')

def index(request):
        return render(request,'monitor/index.html')


# Create Server
def server(request):
    if request.user.is_authenticated():
        if request.method== 'POST':
            form=ServerForm(request.POST)
            if form.is_valid():
                server_name=form.cleaned_data.get('server_name')
                current_user=request.user
                server=Server_User.objects.filter(user_id=current_user.id).values_list('server_id',flat=True)
                for i in range(len(server)):
                    servers=Server.objects.get(id=server[i])
                    if servers.server_name==server_name:
                        return render(request,'registration/server.html',{'message':"You cant create server with same name.",'form':form})
                server=form.save()

                serverobj=Server.objects.get(id=server.id)
                userobj=User.objects.get(id=current_user.id)

                serverUser(serverobj,userobj)
                return redirect('index')
        else:
            form=ServerForm()
        return render(request,'registration/server.html',{'form':form})
    else:
        return redirect('login')

# Singup Controller
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

# Pairing server and user from create server page
def serverUser(serverobj,userobj):
    server_user=Server_User()
    su=server_user.save()
    print(userobj)
    server_user.user_id.add(userobj)
    server_user.server_id.add(serverobj)
    server_user.save()

# Check user and server for pairing to server
@api_view(['GET'])
def checkUser(request):
    if request.method=="GET":
        user=request.GET.get('username')
        pw=request.GET.get('password')
        server_name=request.GET.get('server_name')
        current_user=User.objects.get(username=user) #get user from database by filtering username
        current_server=Server.objects.get(server_name=server_name)#get server from database by filtering server_name
        is_pw=current_user.check_password(pw) #check user password
        if is_pw:
            server_userobj=Server_User.objects.filter(server_id=current_server.id,user_id=current_user.id).exists() #check server user pairing
            if server_userobj:
                return Response(current_server.id)
            return Response(status_code=404)
        return Response(status_code=404)
    return Response(status_code=404)

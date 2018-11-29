from django.http import request, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core import serializers
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from monitor.forms import SignUpForm, ServerForm, ServerUpdateForm
from monitor.models import Ram, Cpu, Disk, Server, ServerUser


def setlanguage(request):
    return render(request, 'set-language.html', {'LANGUAGES': settings.LANGUAGES,
                                                 'SELECTEDLANG': request.LANGUAGE_CODE})


@api_view(['POST', 'OPTIONS'])
def db_save(request):
    # Get request data
    ram = request.GET.getlist('ram', '')
    cpu = request.GET.getlist('cpu', '')
    disk = request.GET.getlist('disk', '')
    server = request.GET.get('server', '')
    # Save given data
    ram_save(ram, server)
    cpu_save(cpu, server)
    disk_save(disk, server)

    return Response(True)


def ram_save(detail, server):
    # get Server objects which id=server
    server = Server.objects.get(id=server)
    last_ram_value = Ram.objects.filter(server_id=server).last()
    if last_ram_value is not None:
        if int(detail[1]) > 2*(last_ram_value.used):
            server_user = ServerUser.objects.filter(server_id=server).values_list('user_id', flat=True)
            user = User.objects.get(id=server_user)
            mail_send(user.email)
    ram = Ram(total=detail[0], used=detail[1], free=detail[2],
              percent=float(detail[3]), sin=detail[4], sout=detail[5],
              server_id=server)  # save data to ram
    ram.save()


def cpu_save(detail, server):
    # get Server objects which id=server
    server = Server.objects.get(id=server)
    last_cpu_value = Cpu.objects.filter(server_id=server).last()
    if last_cpu_value is not None:
        if int(detail[1]) > 2*(last_cpu_value.percent):
            server_user = Server_User.objects.filter(server_id=server).values_list('user_id', flat=True)
            user = User.objects.get(id=server_user)
            mail_send(user.email)

    cpu = Cpu(percent=float(detail[0]), server_id=server)  # save data to cpu
    cpu.save()


def disk_save(detail, server):
    # get Server objects which id=server
    server = Server.objects.get(id=server)
    last_disk_value = Disk.objects.filter(server_id=server).last()
    if last_disk_value is not None:
        if int(detail[1]) > 2*(last_disk_value.used):
            server_user = ServerUser.objects.filter(server_id=server).values_list('user_id', flat=True)
            user = User.objects.get(id=server_user)
            mail_send(user.email)

    # save data to disk
    disk = Disk(total=detail[0], used=detail[1], free=detail[2], percent=float(detail[3]), server_id=server)
    disk.save()


def mail_send(email):
    send_mail("Information", "Subject", "yourmailaddress", [email],
              fail_silently=True)


# Create your views here.
def example_server(request):
    return render(request, 'example/server.html')


def example_howtosetup(request):
    return render(request, 'example/howtosetup.html')


def example_server2_detail(request):
    return render(request, 'example/serverdetail2.html')


def example_server_detail(request):
    return render(request, 'example/serverdetail.html')


def example_detail(request):
    return render(request, 'example/detail.html')


def example_dashboard(request):
    return render(request, 'example/dashboard.html')


def example_chart(request):
    return render(request, 'example/chart.html')


def example_ram_chart(request):
    return render(request, 'example/ramchart.html')


def example_disk_chart(request):
    return render(request, 'example/diskchart.html')


def example_cpu_chart(request):
    return render(request, 'example/cpuchart.html')


def howtosetup(request):
    return render(request, 'monitor/howtosetup.html')


def index(request):
    return render(request, 'monitor/index.html')


def dashboard(request):
    return render(request, 'monitor/dashboard.html')


def server_detail(request, pk):
    current_user = request.user

    # check server user pairing
    server_userobj = ServerUser.objects.filter(user_id=current_user.id,
                                                server_id=pk).exists()
    if server_userobj:
        server = Server.objects.get(id=pk)  # get server
        if request.method == 'POST':
            form = ServerUpdateForm(request.POST)
            if form.is_valid():
                # Get form data
                server_name = form.cleaned_data.get('server_name')
                server_id = form.cleaned_data.get('server_id')
                server_description = form.cleaned_data.get('server_description')

                # Server Update
                server = Server.objects.filter(id=server_id).update(server_name=server_name,
                                                                    server_description=server_description)
                return redirect('server_detail', pk=server_id)
        else:
            form = ServerUpdateForm()

        try:
            ram_values = Ram.objects.filter(server_id=pk)
            cpu_values = Cpu.objects.filter(server_id=pk)
            disk_values = Disk.objects.filter(server_id=pk)
        except(Ram.DoesNotExist, Cpu.DoesNotExist, Disk.DoesNotExist):
            ram_values = None
            cpu_values = None
            disk_values = None
        return render(request, 'monitor/server_detail.html', {
            'server': server,
            'ram': ram_values,
            'cpu': cpu_values,
            'disk': disk_values,
            'form': form
        })
    else:
        return redirect('server')
        # Create Ups! page for here.


def detail(request):
    current_user = request.user

    if request.method == 'POST':
        form = ServerUpdateForm(request.POST)
        if form.is_valid():
            # Get form data
            server_name = form.cleaned_data.get('server_name')
            server_id = form.cleaned_data.get('server_id')
            server_description = form.cleaned_data.get('server_description')

            # check server user pairing
            server_userobj = ServerUser.objects.filter(
                             user_id=current_user.id,
                             server_id=server_id).exists()
            if server_userobj:
                server = Server.objects.filter(id=server_id).update(
                        server_name=server_name,
                        server_description=server_description)  # Server Update
            else:
                pass

            return redirect('detail')
    else:
        form = ServerUpdateForm()

    servers = []
    server = ServerUser.objects.filter(user_id=current_user.id).values_list('server_id', flat=True)
    for i in range(len(server)):
        servers.append(Server.objects.get(id=server[i]))

    return render(request, 'monitor/detail.html',
                  {'form': form, 'servers': servers})


def delete_server(request, pk):
    current_user = request.user

    # check server user pairing
    server_userobj = ServerUser.objects.filter(user_id=current_user.id,
                                                server_id=pk).exists()
    if server_userobj:
        # Update Server
        server = Server.objects.filter(id=pk).update(deleted_at=timezone.now())
    return redirect('detail')


# get Values from database.
'''
    mysql command is: "select * from Ram where server_id=pk orderby id desc 28"
    or this command be like this:
    ram_values = Ram.objects.all() --> get all ram objects
    filtered_ram_values = ram_values.filter(server_id=pk) -->
                          ram_values filter by server_id
    ordered_ram_values = filtered_ram_values.order_by('-id')[:28] -->
                         get ram_values last 28 item
    reversed_ram_values = reversed(ordered_ram_values) -->
                          this command is reversed ram_values
    rams = json_serializer.serialize(reversed_ram_values) -->
            get json from ram_values
'''


def cpuValues(pk):
    json_serializer = serializers.get_serializer("json")()

    cpus = json_serializer.serialize(Cpu.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1],
                                     ensure_ascii=False)
    cpu_exists = Cpu.objects.all().filter(server_id=pk).exists()
    if cpu_exists:
        return cpus
    else:
        return cpu_exists


def ramValues(pk):
    json_serializer = serializers.get_serializer("json")()

    rams = json_serializer.serialize(Ram.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1],
                                     ensure_ascii=False)
    ram_exists = Ram.objects.all().filter(server_id=pk).exists()
    if ram_exists:
        return rams
    else:
        return ram_exists


def diskValues(pk):
    json_serializer = serializers.get_serializer("json")()

    disks = json_serializer.serialize(Disk.objects.all().filter(server_id=pk).order_by('-id')[:28][::-1],
                                      ensure_ascii=False)
    disk_exists = Disk.objects.all().filter(server_id=pk).exists()
    if disk_exists:
        return disks
    else:
        return disk_exists


# chart views here.
def cpu_chart(request, pk):
    cpu_values = cpuValues(pk)
    if cpu_values:
        return render(request, 'monitor/cpu_chart.html', {
            'cpuValues': cpu_values,
        })
    else:
        return redirect('howtosetup')


def disk_chart(request, pk):
    disk_values = diskValues(pk)
    if disk_values:
        return render(request, 'monitor/disk_chart.html', {
            'diskValues': disk_values,
        })
    else:
        return redirect('howtosetup')


def ram_chart(request, pk):
    ram_values = ramValues(pk)
    if ram_values:
        return render(request, 'monitor/ram_chart.html', {
            'ramValues': ram_values,
        })
    else:
        return redirect('howtosetup')


def chart(request, pk):
    cpu_values = cpuValues(pk)
    disk_values = diskValues(pk)
    ram_values = ramValues(pk)

    # if expected data is exists, go to the how to setup.
    if ram_values and cpu_values and disk_values:
        return render(request, 'monitor/chart.html', {
            'ramValues': ram_values,
            'diskValues': disk_values,
            'cpuValues': cpu_values
        })
    else:
        return redirect('howtosetup')


# Create Server
def server(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ServerForm(request.POST)
            if form.is_valid():
                server_name = form.cleaned_data.get('server_name')
                current_user = request.user
                server = ServerUser.objects.filter(user_id=current_user.id).values_list('server_id', flat=True)
                for i in range(len(server)):
                    servers = Server.objects.get(id=server[i])
                    if servers.server_name == server_name:
                        return render(request, 'registration/server.html',
                                      {'message': "You cant create server with same name.", 'form': form})
                server = form.save()

                serverobj = Server.objects.get(id=server.id)
                userobj = User.objects.get(id=current_user.id)

                serverUser(serverobj, userobj)
                return redirect('index')
        else:
            form = ServerForm()
        return render(request, 'registration/server.html', {'form': form})
    else:
        return redirect('login')


# Singup Controller
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('server')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# Pairing server and user from create server page
def serverUser(serverobj, userobj):
    server_user = ServerUser()
    su = server_user.save()  # Create empty ServerUser object for relationship.
    server_user.user_id.add(userobj)
    server_user.server_id.add(serverobj)
    server_user.save()


# Check user and server for pairing to server
@api_view(['GET'])
def check_user(request):
    user = request.GET.get('username')
    pw = request.GET.get('password')
    server_name = request.GET.get('server_name')
    # User exits control.
    userisexist = User.objects.filter(username=user).exists()
    if userisexist:
        # get user from database by filtering username
        current_user = User.objects.get(username=user)
        serverisexist = Server.objects.filter(server_name=server_name).filter()
        if serverisexist:
            # get server from database by filtering server_name
            current_server = Server.objects.get(server_name=server_name)
            # check user password
            is_pw = current_user.check_password(pw)
            if is_pw:
                # check server user pairing
                server_userobj = ServerUser.objects.filter(
                                server_id=current_server.id,
                                user_id=current_user.id).exists()
                if server_userobj:
                    return Response(current_server.id)
                return HttpResponse(status=404)
            return HttpResponse(status=404)
        return HttpResponse(status=404)
    return HttpResponse(status=404)

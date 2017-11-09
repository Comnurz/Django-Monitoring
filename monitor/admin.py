from django.contrib import admin

from .models import Ram,Cpu,Disk,Server
# Register your models here.

admin.site.register(Ram)
admin.site.register(Cpu)
admin.site.register(Disk)
admin.site.register(Server)

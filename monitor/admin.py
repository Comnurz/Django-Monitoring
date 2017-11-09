from django.contrib import admin

from .models import Ram,Cpu,Disk,Server,Server_User
# Register your models here.

class RamAdmin(admin.ModelAdmin):
    list_display=('total','used','free','percent','sin','sout','date')

class CpuAdmin(admin.ModelAdmin):
    list_display=('percent','date')

class DiskAdmin(admin.ModelAdmin):
    list_display=('total','used','free','percent','date')

class ServerAdmin(admin.ModelAdmin):
    list_display=('server_name','ram_id','cpu_id','disk_id','date')

admin.site.register(Ram,RamAdmin)
admin.site.register(Cpu,CpuAdmin)
admin.site.register(Disk,DiskAdmin)
admin.site.register(Server,ServerAdmin)
admin.site.register(Server_User)

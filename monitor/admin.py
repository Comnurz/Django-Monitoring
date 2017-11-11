from django.contrib import admin

from .models import Ram,Cpu,Disk,Server,Server_User

# Display your models details here.
class RamAdmin(admin.ModelAdmin):
    list_display=('total','used','free','percent','sin','sout','date')

class CpuAdmin(admin.ModelAdmin):
    list_display=('percent','date')

class DiskAdmin(admin.ModelAdmin):
    list_display=('total','used','free','percent','date')

# class ServerAdmin(admin.ModelAdmin):
#     list_display=('server_name','ram_link','cpu_link','disk_link','date')

# Register your models here.
admin.site.register(Ram,RamAdmin)
admin.site.register(Cpu,CpuAdmin)
admin.site.register(Disk,DiskAdmin)
admin.site.register(Server)
admin.site.register(Server_User)

from django.contrib import admin
from .models import Ram, Cpu, Disk, Server, ServerUser


# Inlines here
class RamInline(admin.TabularInline):
    model = Ram


class DiskInline(admin.TabularInline):
    model = Disk


class CpuInline(admin.TabularInline):
    model = Cpu


# Display your models details here.
class RamAdmin(admin.ModelAdmin):
    list_display = ('total', 'used', 'free', 'percent', 'sin', 'sout', 'date',
                    'server_link')


class CpuAdmin(admin.ModelAdmin):
    list_display = ('percent', 'date', 'server_link')


class DiskAdmin(admin.ModelAdmin):
    list_display = ('total', 'used', 'free', 'percent', 'date', 'server_link')


class ServerAdmin(admin.ModelAdmin):
    list_display = ('server_name', 'id')
    inlines = [
        RamInline,
        DiskInline,
        CpuInline,
    ]


# Register your models here.
admin.site.register(Ram, RamAdmin)
admin.site.register(Cpu, CpuAdmin)
admin.site.register(Disk, DiskAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(ServerUser)

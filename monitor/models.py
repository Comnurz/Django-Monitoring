from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.template.defaultfilters import escape
from django.core.urlresolvers import reverse

class Ram(models.Model):
    id=models.AutoField(primary_key=True)
    total = models.IntegerField()
    used = models.IntegerField()
    free = models.IntegerField()
    percent = models.FloatField()
    sin = models.IntegerField()
    sout = models.IntegerField()
    date = models.DateTimeField(
           default=timezone.now)

    def __str__(self):
        return str(self.id)

class Cpu(models.Model):
    id=models.AutoField(primary_key=True)
    percent = models.FloatField()
    date = models.DateTimeField(
           default=timezone.now)

    def __str__(self):
        return str(self.id)

class Disk(models.Model):
    id=models.AutoField(primary_key=True)
    total = models.IntegerField()
    used = models.IntegerField()
    free = models.IntegerField()
    percent = models.FloatField()
    date = models.DateTimeField(
           default=timezone.now)

    def __str__(self):
        return str(self.id)

class Server(models.Model):
    id=models.AutoField(primary_key=True)
    ram_id = models.OneToOneField(Ram)
    cpu_id = models.OneToOneField(Cpu)
    disk_id = models.OneToOneField(Disk)
    server_name = models.TextField()
    date = models.DateTimeField(
       default=timezone.now)

    # linked ram_id. Ram_id click event "go to <id> ram update page"
    def ram_link(self):
        return '<a href="%s">%s</a>' % (reverse("admin:monitor_ram_change", args=(self.ram_id,)) , escape(self.ram_id))

    ram_link.allow_tags = True
    ram_link.short_description = "Ram ID"
    
    # linked cpu_id. Cpu_id click event "go to <id> cpu update page"
    def cpu_link(self):
        return '<a href="%s">%s</a>' % (reverse("admin:monitor_cpu_change", args=(self.cpu_id,)) , escape(self.cpu_id))

    cpu_link.allow_tags = True
    cpu_link.short_description = "Cpu ID"

    # linked disk_id. Disk_id click event "go to <id> disk update page"
    def disk_link(self):
        return '<a href="%s">%s</a>' % (reverse("admin:monitor_disk_change", args=(self.disk_id,)) , escape(self.disk_id))

    disk_link.allow_tags = True
    disk_link.short_description = "Disk ID"

    def __str__(self):
            return self.server_name

class Server_User(models.Model):
    id=models.AutoField(primary_key=True)
    server_id=models.ManyToManyField(Server)
    user_id=models.ManyToManyField(User)

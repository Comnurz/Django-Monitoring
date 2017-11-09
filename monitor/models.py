from django.db import models
from django.utils import timezone

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
        return str(self.total)

class Cpu(models.Model):
    id=models.AutoField(primary_key=True)
    percent = models.FloatField()
    date = models.DateTimeField(
           default=timezone.now)

    def __str__(self):
        return str(self.percent)

class Disk(models.Model):
    id=models.AutoField(primary_key=True)
    total = models.IntegerField()
    used = models.IntegerField()
    free = models.IntegerField()
    percent = models.FloatField()
    date = models.DateTimeField(
           default=timezone.now)

    def __str__(self):
        return str(self.total)

class Server(models.Model):
    id=models.AutoField(primary_key=True)
    ram_id = models.OneToOneField(Ram)
    cpu_id = models.OneToOneField(Cpu)
    disk_id = models.OneToOneField(Disk)
    server_name = models.TextField()
    date = models.DateTimeField(
       default=timezone.now)

    def __str__(self):
            return self.server_name

class Server_User(models.Model):
    id=models.AutoField(primary_key=True)
    server_id=models.ManyToManyField(Server)
    user_id=models.ManyToManyField('auth.User')

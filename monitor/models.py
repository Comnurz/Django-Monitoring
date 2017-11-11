from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.template.defaultfilters import escape
from django.core.urlresolvers import reverse


class Server(models.Model):
    id=models.AutoField(primary_key=True)
    server_name = models.TextField()
    date = models.DateTimeField(
       default=timezone.now)

    def __str__(self):
            return self.server_name

class Ram(models.Model):
    id=models.AutoField(primary_key=True)
    total = models.IntegerField()
    used = models.IntegerField()
    free = models.IntegerField()
    percent = models.FloatField()
    sin = models.IntegerField()
    sout = models.IntegerField()
    server_id=models.ForeignKey(Server)
    date = models.DateTimeField(
           default=timezone.now)

    def __str__(self):
        return str(self.id)

class Cpu(models.Model):
    id=models.AutoField(primary_key=True)
    percent = models.FloatField()
    server_id=models.ForeignKey(Server)

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
    server_id=models.ForeignKey(Server)

    date = models.DateTimeField(
           default=timezone.now)

    def __str__(self):
        return str(self.id)

class Server_User(models.Model):
    id=models.AutoField(primary_key=True)
    server_id=models.ManyToManyField(Server)
    user_id=models.ManyToManyField(User)

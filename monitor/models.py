from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.template.defaultfilters import escape
from django.core.urlresolvers import reverse


class Server(models.Model):
    id=models.AutoField(primary_key=True)
    server_name = models.CharField(max_length=255)
    server_description = models.TextField()
    deleted_at=models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(
       default=timezone.now)

    def __str__(self):
            return str(self.id)

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

    # linked server_id. server_id click event "go to <id> server update page"
    def server_link(self):
        return '<a href="%s">%s</a>' % (reverse("admin:monitor_server_change", args=(self.server_id,)) , escape(self.server_id))

    server_link.allow_tags = True
    server_link.short_description = "Server ID"

    def __str__(self):
        return str(self.id)

class Cpu(models.Model):
    id=models.AutoField(primary_key=True)
    percent = models.FloatField()
    server_id=models.ForeignKey(Server)
    date = models.DateTimeField(
           default=timezone.now)

    def server_link(self):
        return '<a href="%s">%s</a>' % (reverse("admin:monitor_server_change", args=(self.server_id,)) , escape(self.server_id))

    server_link.allow_tags = True
    server_link.short_description = "Server ID"

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

    def server_link(self):
        return '<a href="%s">%s</a>' % (reverse("admin:monitor_server_change", args=(self.server_id,)) , escape(self.server_id))

    server_link.allow_tags = True
    server_link.short_description = "Server ID"

    def __str__(self):
        return str(self.id)

class Server_User(models.Model):
    id=models.AutoField(primary_key=True)
    server_id=models.ManyToManyField(Server)
    user_id=models.ManyToManyField(User)

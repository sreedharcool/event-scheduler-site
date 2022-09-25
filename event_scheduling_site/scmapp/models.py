from django.db import models
import datetime
import os


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Event(models.Model):
    eid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    image = models.ImageField(upload_to=filepath, null=True, blank=True)



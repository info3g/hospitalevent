
from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings

from django.contrib.auth.models import Group

class Event_Management(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    event_cateogary = models.ForeignKey(Group, on_delete=models.PROTECT)
    description = models.TextField(max_length=511000)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    date = models.DateField()
    time = models.TimeField()

    def admin_photo(self):
        return '<img src="/site_media/media/{{ Event_Management.Image }}" height="100px" width="100px">'
    admin_photo.allow_tags = True

class EventSelect(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    event = models.ForeignKey(Event_Management, related_name="event_select")
    message = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class eventdismis(models.Model):
#      id = models.AutoField(primary_key=True)
#      message=models.CharField(max_length=200)


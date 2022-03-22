
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    lat_long = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/{self.id}'



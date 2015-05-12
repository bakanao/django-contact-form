from django.db import models


class Contact(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    email = models.CharField(null=False, blank=False, max_length=50)
    ip = models.CharField(null=False, blank=False, max_length=50)
    location = models.CharField(null=False, blank=False, max_length=50)

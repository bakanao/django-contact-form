from django.db import models


class Comments(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    comment = models.TextField(null=False, blank=False, max_length=50)

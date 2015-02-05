from django.db import models


class Url(models.Model):
    original_url = models.URLField(max_length=300)
    custom_shortened_url = models.CharField(max_length=30, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

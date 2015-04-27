from django.contrib.auth.models import User
from django.db import models

from baco import Baco


class Url(models.Model):
    original_url = models.URLField(max_length=300)
    custom_url = models.CharField(null=True, max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.custom_url:
            return '{}: {}'.format(self.custom_url, self.original_url)
        else:
            return '{}: {}'.format(Baco.to_62(self.id), self.original_url)

    def __repr__(self):
        if self.custom_url:
            return '<Url: {}>'.format(self.custom_url)
        else:
            return '<Url: {}>'.format(Baco.to_62(self.id))

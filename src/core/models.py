from django.db import models

from baco import Baco


class Url(models.Model):
    original_url = models.URLField(max_length=300)
    custom_shortened_url = models.CharField(max_length=30, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.custom_shortened_url:
            return '{}: {}'.format(self.custom_shortened_url,
                                   self.original_url)
        else:
            return '{}: {}'.format(Baco.to_62(self.id),
                                   self.original_url)

    def __repr__(self):
        if self.custom_shortened_url:
            return '<Url: %>', self.custom_shortened_url
        else:
            return '<Url: %>', Baco.to_62(self.id)

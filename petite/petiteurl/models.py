from django.db import models

# Create your models here.
from django.db import models


class Urls(models.Model):
    hash_value = models.CharField(unique=True, max_length=8, blank=True, default='')
    url = models.URLField(max_length=600)
    exp_date = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Hash Value: {self.hash_value}," \
               f"URL: {self.url}," \
               f"Expiration date: {self.exp_date}," \
               f"date_added: {self.date_added}," \
               f"count = {self.count}"

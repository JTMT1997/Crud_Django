from django.db import models
from django.urls import reverse

class Data(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('data_edit', kwargs={'pk': self.pk}) 
from django.db import models


class PlantModel(models.Model):
    title = models.CharField('name', max_length=50)
    data = models.TextField('data')

    def __str__(self):
        return self.title


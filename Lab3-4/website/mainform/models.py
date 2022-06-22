from django.db import models


class PlantModel(models.Model):
    title = models.CharField('name', max_length=50)
    data = models.TextField('data')
    cost = models.TextField('cost')
    img = models.ImageField(default='no_image.jpg', upload_to='product.image')

    def __str__(self):
        return self.title

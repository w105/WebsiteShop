from django.db import models
from django.utils.safestring import mark_safe


class PlantModel(models.Model):
    title = models.CharField('name', max_length=50)
    data = models.TextField('data')
    # image = models.ImageField('image', null=True, blank=True, upload_to="PycharmProjects/Lab3-4/Images/")
    #
    # def admin_photo(self):
    #     return mark_safe('<img src="{}" width="100" />' .format(self.image.url))
    # admin_photo.short_description = 'Image'
    # admin_photo.allow_tags = True

    def __str__(self):
        return self.title

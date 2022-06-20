from django.contrib import admin
from.models import PlantModel


admin.site.register(PlantModel)


class DemoProfileAdmin(admin.ModelAdmin):
    fields = ('title', 'data', 'description', 'image')
    list_display = [
        'image',
        'title',
        'data',
        'short_description'
    ]


readonly_fields = 'image'

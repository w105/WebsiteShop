# Generated by Django 4.0.5 on 2022-06-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='PycharmProjects/Lab3-4/Images/'),
        ),
        migrations.AlterField(
            model_name='plantmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_images_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='title',
            field=models.CharField(default='', max_length=80, verbose_name='标题'),
        ),
    ]

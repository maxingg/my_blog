# Generated by Django 2.1.3 on 2018-11-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/portraits/%Y'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-15 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_moviedata_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedata',
            old_name='img',
            new_name='image',
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_moviedata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='img',
            field=models.ImageField(default='Images/None/noimg.jpg', upload_to='Images/'),
        ),
    ]
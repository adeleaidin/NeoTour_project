# Generated by Django 4.2.13 on 2024-06-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(upload_to='user_photos/'),
        ),
    ]

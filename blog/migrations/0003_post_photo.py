# Generated by Django 2.0.6 on 2018-07-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog/post/%y/%m/%d'),
        ),
    ]

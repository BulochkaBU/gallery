# Generated by Django 3.2.8 on 2021-10-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_auto_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='comments',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='auto',
            name='like',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

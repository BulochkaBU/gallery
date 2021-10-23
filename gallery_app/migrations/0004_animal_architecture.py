# Generated by Django 3.2.8 on 2021-10-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0003_auto_20211023_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='animal_images')),
                ('comments', models.CharField(blank=True, max_length=200)),
                ('like', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Architecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='architecture_images')),
                ('comments', models.CharField(blank=True, max_length=200)),
                ('like', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]

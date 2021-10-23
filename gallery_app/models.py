from django.db import models

from gallery_project.settings import MEDIA_AUTO_IMAGE_DIR, MEDIA_ARCHITECTURE_IMAGE_DIR, MEDIA_ANIMAL_IMAGE_DIR


class Auto(models.Model):
    """Auto Model."""
    picture = models.ImageField(upload_to=MEDIA_AUTO_IMAGE_DIR)
    comments = models.CharField(max_length=200, blank=True)
    like = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.comments}'


class Animal(models.Model):
    """Animal Model."""
    picture = models.ImageField(upload_to=MEDIA_ANIMAL_IMAGE_DIR)
    comments = models.CharField(max_length=200, blank=True)
    like = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.comments}'


class Architecture(models.Model):
    """Architecture Model."""
    picture = models.ImageField(upload_to=MEDIA_ARCHITECTURE_IMAGE_DIR)
    comments = models.CharField(max_length=200, blank=True)
    like = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.comments}'

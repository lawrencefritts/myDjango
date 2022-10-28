from django.db import models

PUB_CHOICES = (
    ("Dark Horse Comics", "Dark Horse Comics"),
    ("DC", "DC"),
    ("Marvel", "Marvel")
)

class Publisher(models.Model):
    pub_name = models.CharField(
        max_length=20,
        choices=PUB_CHOICES,
        blank=True
    ) 

class ComicBook(models.Model):
    series_number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    
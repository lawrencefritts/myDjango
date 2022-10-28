from django.db import models

BOOK_TYPES = (
    ("fic", "Fiction"),
    ("scifi", "SciFi"),
    ("fantsy", "Fantsy"),
)

class Publisher(models.Model):
    name = models.CharField(max_length=30)

class Author(models.Model):
    name = models.CharField(max_length=50)

class Series(models.Model):
    series_name = models.CharField(max_length=50)
    series_type = models.CharField(max_length=10)

class Book(models.Model):
    title = models.CharField(max_length=50)
    cpywrite = models.SmallIntegerField()

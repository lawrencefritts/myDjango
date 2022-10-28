from django.db import models

DIFFICULTY_CHOICES = (
    ("Easy", "Easy"),
)

PLANT_SIZE_CHOICES = (
    ("Compact", "Compact"),
)

RANK_CHOICES = (
    ("Excellent", "Excellent"),
    ("Good", "Good"),
    ("Mediocre", "Mediocre"),
    ("Avoid", "Avoid"),
)

class Producer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    cannibas_store = models.BooleanField(default=False)

class StoreCannibas(models.Model):
    name = models.CharField(max_length=100)
    producer = models.CharField(max_length=25)

class Seed(models.Model):
    name = models.CharField(max_length=50)
    indica_percent = models.IntegerField()
    sative_percent = models.IntegerField()
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='Easy'
    )
    thc = models.IntegerField()
    cbd = models.IntegerField()
    seed_producer = models.ForeignKey(Producer, null=False, on_delete=models.CASCADE)

class Plant(models.Model):
    seed = models.ForeignKey(Seed, null=False, on_delete=models.CASCADE)
    size = models.CharField(
        max_length=10,
        choices=PLANT_SIZE_CHOICES,
        default='Compact'
    )
    veg_state = models.CharField(max_length=50)
    flower_state = models.CharField(max_length=50)
    yields = models.CharField(max_length=50)
    
class FlowerRank(models.Model):
    name = models.ForeignKey(StoreCannibas, null=False, on_delete=models.CASCADE)
    lfd_rank = models.CharField(
        max_length=15,
        choices=RANK_CHOICES,
        null=True 
    )
    dlf_rank = models.CharField(
        max_length=15,
        choices=RANK_CHOICES,
        null=True 
    )
    hrf_rank = models.CharField(
        max_length=15,
        choices=RANK_CHOICES,
        null=True 
    )
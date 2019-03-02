from django.db import models

# Create your models here.

BODY_TYPE_CHOICES = (
    ("sedan","sedan"),
    ("combi","combi"),
    ("hatchback", "hatchback"),
    ("cabrio", "cabrio"),
    ("van", "van")
)

class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    body_type = models.CharField(max_length=100, choices=BODY_TYPE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.brand}|{self.model}|{self.year}|{self.body_type}"
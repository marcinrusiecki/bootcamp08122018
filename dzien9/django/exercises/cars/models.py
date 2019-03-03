from django.db import models

# Create your models here.

BODY_TYPE_CHOICES = (
    ("sedan","sedan"),
    ("combi","combi"),
    ("hatchback", "hatchback"),
    ("cabrio", "cabrio"),
    ("van", "van")
)

ENGINE_TYPE_CHOICES = (
    ("electric","electric"),
    ("diesel","diesel"),
    ("benz", "benz"),
    ("hybrid", "hybrid"),
)


class Engine(models.Model):
    type = models.CharField(max_length=100, choices=ENGINE_TYPE_CHOICES)
    power = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type}|{self.power}|{self.description}"

class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    body_type = models.CharField(max_length=100, choices=BODY_TYPE_CHOICES, null=True, blank=True)
    engine = models.ForeignKey(Engine, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand}|{self.model}|{self.year}|{self.body_type}"



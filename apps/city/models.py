from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default="Maharashtra")

    def __str__(self):
        return self.name

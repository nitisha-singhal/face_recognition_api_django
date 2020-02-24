from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='users/%Y/%m/%d/')

    def __str__(self):
        return self.name


class PersonMatch(models.Model):
    image = models.ImageField(upload_to='requests/%Y/%m/%d/')

    def __str__(self):
        return self.image.name

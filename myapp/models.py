from django.db import models

class PersonModel(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

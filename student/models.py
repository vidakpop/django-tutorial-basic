from django.db import models

#creating a student profile model

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

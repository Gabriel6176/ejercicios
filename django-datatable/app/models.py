from django.db import models

# Create your models here.
class Programmer(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=30)
    birthdate=models.CharField(max_length=10)

    class Meta:
        db_table = "programmer"
        
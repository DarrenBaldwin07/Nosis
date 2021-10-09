from django.db import models

# Create your models here.
class User_data(models.Model):
    sex = models.TextField(null=False)
    age = models.IntegerField(null=False)

    

    
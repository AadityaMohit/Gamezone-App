from django.db import models


# Create your models here.
class Signin(models.Model):
    name=models.CharField(max_length=12)
    email=models.EmailField()
    phone=models.CharField(max_length=30)
    def __str__(self):
        return self.name
# after adding home app in setting use migrations command to create the table makemigrations->it will sql info of the data 
# -> makemigrate->it will ceate table
class Login(models.Model):
    email=models.EmailField()
    password=models.IntegerField()
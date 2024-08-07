from django.db import models

# Create your models here.
class Orders(models.Model):
    sno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    price = models.FloatField()
    mail = models.EmailField()
    address = models.CharField(max_length=50)
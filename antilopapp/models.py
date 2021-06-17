from django.db import models
 #Create your models here.
class pickup(models.Model):
     image=models.ImageField()
     contact_number = models.CharField(max_length=12)
     contact_name = models.CharField(max_length=100)
     address = models.TextField(max_length=500)
     city = models.CharField(max_length=100,blank=True,null=True)
     pin_code = models.IntegerField(default="43701")
     weight = models.IntegerField()
     pracel_type = models.CharField(max_length=500)

class Query(models.Model):
    contact_name=models.CharField(max_length=12)
    contact_number=models.IntegerField()
    address=models.TextField(max_length=100)
    requirement=models.CharField(max_length=60)
    city=models.CharField(max_length=50)
    pin_code=models.IntegerField()
    apllied=models.CharField(max_length=50)

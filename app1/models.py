from django.db import models

# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()   
    phone=models.CharField(max_length=10)
    month=models.IntegerField()
    date=models.IntegerField()
    size=models.IntegerField()
    flavour=models.CharField(max_length=25)
    code=models.CharField(max_length=5,null=False)
    description=models.TextField(max_length=50)


class Order(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()   
    phone=models.CharField(max_length=10)
    month=models.IntegerField()
    date=models.IntegerField()
    size=models.IntegerField()
    flavour=models.CharField(max_length=25)
    code=models.CharField(max_length=5,null=False)
    description=models.TextField(max_length=50)





class Purchase(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()   
    phone=models.CharField(max_length=10)
    month=models.IntegerField()
    date=models.IntegerField()
    size=models.IntegerField()
    flavour=models.CharField(max_length=25)
    code=models.CharField(max_length=5,null=False)
    description=models.TextField(max_length=50)






class Buy(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()   
    phone=models.CharField(max_length=10)
    month=models.IntegerField()
    date=models.IntegerField()
    size=models.IntegerField()
    flavour=models.CharField(max_length=25)
    code=models.CharField(max_length=5,null=False)
    description=models.TextField(max_length=50)






class Feedback(models.Model):
    rate=models.CharField(max_length=10)
    comments=models.CharField(max_length=25)   
    name=models.CharField(max_length=10)
    email=models.EmailField()
    
    





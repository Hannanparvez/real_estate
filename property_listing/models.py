from django.db import models

from datetime import datetime
from agents.models import Agent

class Property_listing(models.Model):
    sale_type=models.CharField(max_length=200,default="rent")
    agent=models.ForeignKey(Agent,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    property_type=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=20)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2, decimal_places=1)
    garage=models.IntegerField(default=0)
    area=models.IntegerField()
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    cover=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    status=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    slider=models.BooleanField(default=False)

    def __str__(self):
        return self.title
class Testimonial(models.Model):
    family_name=models.CharField(max_length=200)
    family_photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    family_review=models.TextField()

    def __str__(self):
        return self.family_name

class Inquire(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=300)
    message=models.TextField()
    agent=models.CharField(max_length=300)
    property_name=models.CharField(max_length=300)


    def __str__(self):
        return self.email

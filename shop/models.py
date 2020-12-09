from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Media(models.Model):
    instagram = models.CharField(max_length=255,null=True,default="comming soon")
    Website = models.CharField(max_length=255,null=True,default="comming soon")
    Facebook = models.CharField(max_length=255,null=True,default="comming soon")
    Twitter = models.CharField(max_length=255,null=True,default="comming soon")


class ContactInfo(models.Model):
    telno= models.CharField(max_length=20)
    social_sites =models.ForeignKey(Media,null=True,on_delete=models.CASCADE)


class Category(models.Model):
    category = models.CharField(max_length=255)

class Business(models.Model):
    name = models.CharField(max_length=255)
    photo = CloudinaryField('image')
    hours = models.CharField(max_length=255,null=False)
    price_range = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    other_details=models.TextField()
    location=models.CharField(default="enter location details",null='False',max_length=255)
    contactInfo = models.OneToOneField(ContactInfo,null = True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    email = models.EmailField()
    review = models.IntegerField (default=0,blank=True, null=True)
    comment = models.TextField()




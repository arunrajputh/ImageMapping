from django.db import models

class Profile1(models.Model):
    first_name =models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic =models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    age=models.PositiveIntegerField()
    mail=models.CharField(max_length=20)
    mobile = models.CharField(max_length=20,null=False)
    

class Profile_user(models.Model):
    first_name =models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic =models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    age=models.PositiveIntegerField()
    mail=models.CharField(max_length=20)
    mobile = models.CharField(max_length=20,null=False)
    
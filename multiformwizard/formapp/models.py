from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class UserApplication(models.Model):
    title = models.CharField(max_length=250, null=True,blank=True)
    first_name = models.CharField(max_length=250,null=True,blank=True)
    surname = models.CharField(max_length=250,null=True,blank=True)
    d_o_b = models.DateField(null=True,blank=True)
    company_name=models.CharField(max_length=250,null=True,blank=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    telephone = PhoneNumberField(null=True,blank=True)
    bidding_settings = models.CharField(max_length=250, null=True,blank=True)
    google_id = models.IntegerField()

    def __str__(self):
        return self.title
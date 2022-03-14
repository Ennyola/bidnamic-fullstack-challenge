from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Account(models.Model):
    title = models.CharField(max_length=250, null=True)
    first_name = models.CharField(max_length=250,null=True)
    surname = models.CharField(max_length=250,null=True)
    d_o_b = models.DateField(null=True)
    address = models.CharField(max_length=250,null=True)
    telephone = PhoneNumberField(blank=True)
    bidding_settings = models.CharField(max_length=250,null=True)
    google_id = models.IntegerField()

    def __str__(self):
        return self.title
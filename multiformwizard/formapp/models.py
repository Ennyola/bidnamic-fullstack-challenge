from django.db import models

# Create your models here.


class Account(models.Model):
    title = models.CharField(max_length=250, null=True)
    first_name = models.CharField(max_length=250,null=True)
    surname = models.CharField(max_length=250,null=True)
    d_o_b = models.DateField(null=True)
    address = models.CharField(max_length=250,null=True)
    telephone = models.CharField(max_length=250,null=True)
    bidding_settings = models.CharField(max_length=250,null=True)
    google_id = models.IntegerField()

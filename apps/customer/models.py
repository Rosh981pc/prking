from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
   

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=True)
    tax_id = models.TextField(blank=True, default="C/F")
    address = models.TextField(blank=True, default="Ciudad")
    

    def __str__(self):
        return self.name + " " + self.last_name


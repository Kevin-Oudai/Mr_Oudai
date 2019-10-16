from django.db import models
from django.urls import reverse

class ContactMe(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=120, null=True)
    message = models.TextField(null=True)

    
    

    


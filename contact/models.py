from django.db import models

class contato(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=1000, blank=False)

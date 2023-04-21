from django.db import models
from django.contrib.auth.models import User

class contato(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=1000, blank=False)
    read = models.BooleanField(default=False, verbose_name='Visto')

    def __str__(self):
        return f'contato de {self.name}'


class read_contato(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.ForeignKey(contato, on_delete=models.CASCADE)

    def __str__(self):
        return f'O {self.user} verificou o contato de {self.read.name}'

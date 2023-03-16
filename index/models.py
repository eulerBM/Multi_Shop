from django.db import models
from django.contrib.auth.models import User


# Produto
class product(models.Model):
    choices_status = (
        ('Eletrodoméstico', 'Eletrodoméstico'),
        ('Beleza', 'Beleza'),
        ('Acessórios', 'Acessórios'),
        ('Roupas', 'Roupas'),
        ('Fantasias', 'Fantasias'),
        ('Computador', 'Computador'),

    )
    name = models.CharField(max_length=50, blank=False)
    category = models.CharField(choices=choices_status, max_length=20 ,default='Categoria')
    description = models.TextField(max_length=250, blank=False)
    observation = models.TextField(max_length=150, blank=False)
    price = models.FloatField(blank=False)
    stock = models.IntegerField(blank=False, default='0')
    image = models.ImageField(upload_to="image/", blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

# Review
class review_person(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    product_review = models.ForeignKey(product, on_delete=models.CASCADE, default="")
    text = models.TextField(max_length=150, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person.get_username().upper()} / {self.product_review} "


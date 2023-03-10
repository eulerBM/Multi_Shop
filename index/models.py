from django.db import models
from django.contrib.auth.models import User



# Review
class review_person(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)


# Produto
class product(models.Model):
    choices_status = (
        ('Eletrodoméstico', 'Eletrodoméstico'),
        ('Beleza', 'Beleza'),
        ('Acessórios', 'Acessórios'),
        ('Roupas', 'Roupas'),

    )
    name = models.CharField(max_length=50, blank=False)
    category = models.CharField(choices=choices_status, max_length=20 ,default='Categoria')
    description = models.TextField(max_length=250, blank=False)
    observation = models.TextField(max_length=150, blank=False)
    price = models.FloatField(blank=False)
    review = models.ManyToManyField(review_person)
    image = models.ImageField(upload_to="image/", blank=False)

    def __str__(self):
        return self.name


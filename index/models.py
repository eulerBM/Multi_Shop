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
    choices_size = (
        ('Não informar', 'Não informar'),
        ('pp', 'pp'),
        ('p', 'p'),
        ('m', 'm'),
        ('g', 'g'),
        ('gg', 'gg'),
        ('xgg', 'xgg'), 

    )
    choices_color = (
        ('Não informar', 'Não informar'),
        ('Preto', 'Preto'),
        ('Branco', 'Branco'),
        ('Vermelho', 'Vermelho'),
        ('Azul', 'Azul'),
        ('Verde', 'Verde'),
        

    )

    name = models.CharField(max_length=50, blank=False, verbose_name='Nome')
    category = models.CharField(choices=choices_status, max_length=20 ,default='Categoria', verbose_name='Categoria')
    description = models.TextField(max_length=250, blank=False, verbose_name='descrição')
    observation = models.TextField(max_length=150, blank=False, verbose_name='Observação')
    price = models.FloatField(blank=False, verbose_name='Preço')
    stock = models.IntegerField(blank=False, default='0', verbose_name='Estoque')
    image = models.ImageField(upload_to="image/", blank=False, default='image/')
    likes = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
    active = models.BooleanField(default=True, verbose_name='Situação')
    color = models.CharField(choices=choices_color, blank=False, max_length=15, default='Não informar')
    size = models.CharField(choices=choices_size, max_length=13 ,default='size', blank=False, verbose_name='Tamanho')
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


#Carrinho de compras
class carrinho(models.Model):
    car_user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_product = models.ManyToManyField(product, blank=True )

    def __str__(self):
        return f"Carrinho de {self.car_user}"
    


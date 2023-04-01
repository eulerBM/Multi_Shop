from django.test import TestCase
from index.models import *


class teste_models_index(TestCase):

    def setUp(self):

        product.objects.create(
            name='pc',
            category= 'Computador',
            description='muito bom o pc',
            observation='é rapido pakas',
            price=100,
            stock='4',
            image='image/'
        )

    def test_models_name_product_name(self):
        produto_ = product.objects.get(id=1)

        self.assertEqual(produto_.name, 'pc')
        self.assertEqual(len(produto_.name), 2)

        max_len = produto_._meta.get_field('name').max_length
        self.assertEqual(max_len, 50)

        max_verbo = produto_._meta.get_field('name').verbose_name
        self.assertEqual(max_verbo, 'name')
        
        
    def test_models_name_product_category(self):
        produto_ = product.objects.get(id=1)

        self.assertEqual(produto_.category, 'Computador')
        self.assertEqual(len(produto_.category), 10)

        max_len = produto_._meta.get_field('category').max_length
        self.assertEqual(max_len, 20)

    def  test_models_name_product_description(self):
        produto_ = product.objects.get(id=1)

        self.assertEqual(produto_.description, 'muito bom o pc' )

        max_len = produto_._meta.get_field('description').max_length
        self.assertEqual(max_len, 250)

    def test_models_name_product_observation(self):
        produto_ = product.objects.get(id=1)

        self.assertEqual(produto_.observation, 'é rapido pakas' )

        max_len = produto_._meta.get_field('observation').max_length
        self.assertEqual(max_len, 150)

    def test_models_name_product_price(self):
        produto_ = product.objects.get(id=1)

        self.assertEqual(produto_.price, float(100) )

        max_len = produto_._meta.get_field('price').max_length
        self.assertEqual(max_len, None)

    def test_models_name_product_stock(self):
        produto_ = product.objects.get(id=1)

        self.assertEqual(produto_.stock, int(4) )

        max_len = produto_._meta.get_field('stock').max_length
        self.assertEqual(max_len, None)

    def test_models_name_product_image(self):
        produto_ = product.objects.get(id=1)

        self.assertEqual(produto_.image, 'image/' )

        max_len = produto_._meta.get_field('image').max_length
        self.assertEqual(max_len, int(100))

    def test_models_name_product_likes(self):
        produto_ = product.objects.get(id=1)

        self.assertEqual(produto_.likes, None )

        max_len = produto_._meta.get_field('likes').max_length
        self.assertEqual(max_len, None)

    



        
        


        
        
        


    
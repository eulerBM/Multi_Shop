from django.test import TestCase
from index.views import *
from index.models import *
from django.urls import reverse


class teste_views_index(TestCase):  

    def setUp(self):

        produto = product.objects.create(
            name='pc',
            category= 'Computador',
            description='muito bom o pc',
            observation='é rapido pakas',
            price=100,
            stock='4',
            image='image/'
        )


    def test_views_name_index(self):
       response_get = self.client.get(reverse('index'))
       self.assertEqual(response_get.status_code, 200)
       response_post = self.client.post(reverse('index'))
       self.assertEqual(response_post.status_code, 200)
       self.assertTemplateUsed(response_get, 'index.html')
       self.assertEqual(product.objects.all()[:1].count(), 1)
       

    def test_views_name_add_car(self):
        response = self.client.get(reverse(add_car, args=[1]))
        self.assertTrue(response)
        self.assertRedirects(response, '/accounts/login/?next=/carrinho/1')
        self.assertNotEqual(response, 'index')
        
        response_pos = self.client.post(reverse(add_car, args=[1]))
        self.assertEqual(response_pos.status_code, 405)
        self.assertTemplateNotUsed(response_pos, 'signup',  'logout' )
       

    
        
        


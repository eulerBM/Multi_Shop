from django.test import TestCase , Client
from django.urls import reverse
from index.views import *


class Teste_urls(TestCase):

    def setUp(self):
        self.client = Client()



    def test_url_name_index(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_url_name_add_car(self):
        response = self.client.get(reverse('add_car', args=[6]))
        self.assertEqual(response.status_code, 302)
       
    def test_url_name_like_product(self):
        response = self.client.get(reverse('like_product', args=[5]))
        self.assertEqual(response.status_code, 302)
        

       
        
        


        

        

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIClient

from fixtures.utils import get_fixtures

from apps.product.models import Product

class ProductAPI(TestCase):

    fixtures = get_fixtures()

    def test_bill_product(self):
        client = APIClient()
        products = Product.objects.all()
        response = client.get(reverse('product:api:bill'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(products.count(), len(response.data['list']))

        price_total = 0
        tax_total = 0
        grand_total = 0

        for product in products:
            price_total += product.price
            tax_total += product.tax()
            grand_total += product.amount()
        
        self.assertEqual(price_total, response.data['price_subtotal'])
        self.assertEqual(tax_total, response.data['tax_subtotal'])
        self.assertEqual(grand_total, response.data['grand_subtotal'])

    def test_list_product(self):
        client = APIClient()
        product = Product.objects.all()
        response = client.get(reverse('product:api:list'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(product.count(), len(response.data))

    def test_create_product(self):
        client = APIClient()
        product_id = Product.objects.first().id
        data = {
            'name': 'test',
            'tax_code': '1',
            'price': 10000
        }
        response = client.post(reverse('product:api:list'), data, format='json')
        self.assertEqual(201, response.status_code)
        product = Product.objects.last()
        self.assertEqual(product.id, response.data['id'])
        self.assertEqual(product.name, 'test')
        
    def test_update_product(self):
        client = APIClient()
        product = Product.objects.first()
        product_id = product.id
        new_title = 'copy of ' + product.name
        data = {
            'name': new_title
        }
        response = client.put(reverse('product:api:detail', args=[product.id]), data, format='json')
        self.assertEqual(200, response.status_code)
        product = Product.objects.filter(name=new_title)
        self.assertTrue(product.exists())
        self.assertEqual(product_id, response.data['id'])
        
    def test_delete_product(self):
        client = APIClient()
        product = Product.objects.first()
        product_id = product.id
        response = client.delete(reverse('product:api:detail', args=[product.id]))
        self.assertEqual(204, response.status_code)
        self.assertFalse(Product.objects.filter(pk=product_id).exists())


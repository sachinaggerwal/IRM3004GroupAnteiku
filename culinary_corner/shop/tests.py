'''
This is the tests module
'''
from django.test import TestCase
from .apps import ShopConfig
from .models import Product,Contact,Orders,OrderUpdate
from datetime import date
# Create your tests here.
class ShopConfigTest(TestCase):
    def test_app_name(self):
        self.assertEqual(ShopConfig.name,"shop")

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            product_name = "test product",
            category = "test",
            desc = "test description",
            price = 10,
            pub_date = date.today()
        )

    def test_product_name_label(self):
        product = Product.objects.get(id = 1)
        field_label = product._meta.get_field('product_name').verbose_name
        self.assertEquals(field_label,"product name")
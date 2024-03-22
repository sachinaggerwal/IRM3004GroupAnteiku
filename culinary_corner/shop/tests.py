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

class ContactModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(
            name = "test user",
            email = "test@example.com",
            phone = "123-456-7890",
            desc = "test message"
        )

    def test_contact_name_label(self):
        contact = Contact.objects.get(msg_id = 1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEquals(field_label,"name")

class OrdersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Orders.objects.create(
            amount = 10,
            name = "test user",
            email = "test@example.com",
            address = "10 Test Place",
            city = "test city",
            state = "CA",
            zip_code = "K1J 101",
            phone = "123-456-7890",
        )

    def test_orders_name_label(self):
        order = Orders.objects.get(order_id = 1)
        field_label = order._meta.get_field('items_json').verbose_name
        self.assertEquals(field_label,"items json")

class OrderUpdateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        OrderUpdate.objects.create(
            order_id = 1,
            update_desc = "example text",
            timestamp = date.today()
        )

    def test_update_desc_label(self):
        orderUpdate = OrderUpdate.objects.get(order_id = 1)
        field_label = orderUpdate._meta.get_field('update_desc').verbose_name
        self.assertEquals(field_label, 'update desc')
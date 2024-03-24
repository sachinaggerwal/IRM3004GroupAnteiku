'''
This is the tests module
'''
from django.test import TestCase
from .apps import ShopConfig
from .models import Product,Contact,Orders,OrderUpdate
from datetime import date
from django.urls import reverse
from django.conf import settings
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

class TestViews(TestCase):
    def setUp(self):
        pass

    def test_index_view(self):
        response = self.client.get(reverse('ShopHome'))
        self.assertEqual(response.status_code,200)

    def test_search_view(self):
        response = self.client.get(reverse('Search'))
        self.assertEqual(response.status_code,200)
    
    def test_about_view(self):
        response = self.client.get(reverse('AboutUs'))
        self.assertEqual(response.status_code,200)

    def test_faq_view(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code,200)
    
    def test_contact_view_get(self):
        response = self.client.get(reverse('ContactUs'))
        self.assertEqual(response.status_code,200)
    
    def test_contact_view_post(self):
        response = self.client.post(reverse('ContactUs'),
                                    {
                                        'name' : 'John Doe',
                                        'email' : 'john@example.com',
                                        'phone' : '1234567890',
                                        'desc' : 'this is a test message'
                                    }
                                    )
        self.assertEqual(response.status_code,200)
    
    def test_tracker_view_get(self):
        response = self.client.get(reverse('TrackingStatus'))
        self.assertEqual(response.status_code,200)

    def test_tracker_view_post(self):
        response = self.client.post(reverse('TrackingStatus'),
                                    {
                                        'order_id' : '123',
                                        'email' : 'john@example.com'
                                    }
                                    )
        self.assertEqual(response.status_code,200)
    
    def test_checkout_view_get(self):
        response = self.client.get(reverse('Checkout'))
        self.assertEqual(response.status_code,200)

class SettingsTest(TestCase):
    def test_secret_key_set(self):
        self.assertTrue(settings.SECRET_KEY)
    
    def test_allowed_hosts_set(self):
        self.assertTrue(settings.ALLOWED_HOSTS)
    
    def test_installed_apps(self):
        self.assertIn('shop.apps.ShopConfig',settings.INSTALLED_APPS)
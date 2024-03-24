'''
creating different views and paths
'''
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.product_view, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("faq/", views.faq, name="faq"),
    path("african/", views.african, name="africanWepage"),
    path("america/", views.america, name="americanWepage"),
    path("asia/", views.asia, name="asiaWepage"),
    path("euro/", views.euro, name="euroWepage"),
    path("mediterrarean/", views.mediterrarean, name="mediterrarreanWepage")
]
